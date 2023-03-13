import React, { useState, useEffect, useRef, forwardRef } from 'react'
import optimize from 'svgo-browser/lib/optimize'
import { getCsrfToken } from './auth/auth_manager'
import fmtSeconds from './util'
import * as c2s from './canvas2svg'

var currX, currY, prevY, prevX = 0;
var flag, dotFlag = false;

const CommentSection = forwardRef((props, canvasRef) => {
    const player = props.player;
    const videoId = props.videoId;
    const viewedNote = props.viewedNote;
    const annotating = props.annotating;
    const setAnnotating = props.setAnnotating;
    const setViewedNote = props.setViewedNote;

    const [comments, setComments] = useState([]);
    const [curTime, setCurTime] = useState(0);

    const commentTextRef = useRef(null);

    const c2sCtxRef = useRef(null);

    let fetchComments = () => {
        fetch(`/api/comments/${videoId}`).then((resp) => {
            return resp.json();
        }).then((json) => {
            setComments(json);
        })
    }
 
    useEffect(() => {
        fetchComments();
    }, []);

    let draw_on_canvas = (ctx1, ctx2) => {
        ctx1.beginPath();
        ctx1.moveTo(prevX, prevY);
        ctx1.lineTo(currX, currY);
        ctx1.stroke();
        ctx1.closePath();

        ctx2.beginPath();
        ctx2.moveTo(prevX, prevY);
        ctx2.lineTo(currX, currY);
        ctx2.stroke();
        ctx2.closePath();
    }

    let findxy = (ctx1, ctx2, res, e) => {
        if (res == 'down') {
            prevX = currX;
            prevY = currY;
            currX = e.x;
            currY = e.y;
    
            flag = true;
            dotFlag = true;
            if (dotFlag) {
                ctx1.beginPath();
                ctx1.fillStyle = 'yellow';
                ctx1.fillRect(currX, currY, 2, 2);
                ctx1.closePath();
                ctx2.beginPath();
                ctx2.fillStyle = 'yellow';
                ctx2.fillRect(currX, currY, 2, 2);
                ctx2.closePath();
                dotFlag = false;
            }
        }
        if (res == 'up' || res == "out") {
            flag = false;
        }
        if (res == 'move') {
            if (flag) {
                prevX = currX;
                prevY = currY;
                currX = e.x;
                currY = e.y;
                draw_on_canvas(ctx1, ctx2);
            }
        }
    }

    useEffect(() => {
        if (annotating) {
            let canv = canvasRef.current;
            canv.width = canv.clientWidth;
            canv.height = canv.clientHeight;
            let canvCtx = canv.getContext('2d')
            let c2sCtx = new C2S(canv.width, canv.height);
            c2sCtxRef.current = c2sCtx;
            canvCtx.clearRect(0, 0, canv.width, canv.height);
            c2sCtx.clearRect(0, 0, canv.width, canv.height);
            let getCursorPosition = (canvas, event) => {
                const rect = canvas.getBoundingClientRect()
                const x = event.clientX - rect.left
                const y = event.clientY - rect.top
                return {x: x, y: y}
            }
            canvCtx.strokeStyle = 'yellow';
            c2sCtx.strokeStyle = 'yellow';
            canvCtx.lineWidth = 5;
            c2sCtx.lineWidth = 5;
            canv.addEventListener("mousemove", function (e) {
                findxy(canvCtx, c2sCtx, 'move', getCursorPosition(canv, e))
            }, false);
            canv.addEventListener("mousedown", function (e) {
                findxy(canvCtx, c2sCtx, 'down', getCursorPosition(canv, e))
            }, false);
            canv.addEventListener("mouseup", function (e) {
                findxy(canvCtx, c2sCtx, 'up', getCursorPosition(canv, e))
            }, false);
            canv.addEventListener("mouseout", function (e) {
                findxy(canvCtx, c2sCtx, 'out', getCursorPosition(canv, e))
            }, false);
        }
    }, [annotating])

    useEffect(() => {
        const interval = setInterval(() => {
            if (player != null) {
                cur = ~~player.getCurrentTime() // ~~ is shorthand for Math.floor
                setCurTime(cur);
            }
        }, 100);
        return () => clearInterval(interval);
    }, [player])

    let toggleAnnotating = () => {
        if (!annotating && player != null) {
            player.pauseVideo();
        }
        setAnnotating(!annotating);
    }

    let saveAnnotation = async () => {
        let canv = canvasRef.current;
        let dataUrl = canv.toDataURL('image/jpg', 0.5);
        console.log('base64:', dataUrl.length);
        // Create a link
        var aDownloadLink = document.createElement('a');
        // Add the name of the file to the link
        aDownloadLink.download = 'canvas_image.jpg';
        // Attach the data to the link
        aDownloadLink.href = dataUrl;
        // Get the code to click the download link
        aDownloadLink.click();

        let serializedSvg = c2sCtxRef.current.getSerializedSvg(true);
        let optimized = await optimize(serializedSvg);
        let doubleOptimized = await optimize(optimized);
        let tripleOptimized = await optimize(doubleOptimized);
        // console.log(optimized);
        console.log('optimized svg: ', doubleOptimized.length);
        // console.log(tripleOptimized)
        // console.log(optimized.length, doubleOptimized.length, tripleOptimized.length)
    }

    let showComment = (comment) => {
        player.seekTo(comment.timestamp);
        player.playVideo();
        if (comment.annotation != '') {
            player.pauseVideo();
        }
        if (annotating) {
            toggleAnnotating();
        }
        setViewedNote(comment.annotation);
    }

    let postComment = async () => {
        let annotation = '';
        if (annotating) {
            let serializedSvg = c2sCtxRef.current.getSerializedSvg(true);
            let optimized = await optimize(serializedSvg);
            annotation = await optimize(optimized);
            toggleAnnotating();
        }

        let text = commentTextRef.current.value;
        if (text == '') {
            text = 'Nice play!';
        }
        let timestamp = curTime;
        let data = new FormData();
        data.append('text', text);
        data.append('timestamp', timestamp);
        data.append('annotation', annotation);
        data.append('video_id', videoId);

        fetch('/api/comments/' + videoId + '/', {
            'method': 'POST',
            'body': data,
            'headers': {
                'X-CSRFToken': getCsrfToken(),
            }
        }).then((resp) => {
            console.log(resp)
            return resp.json()
        }).then((json) => {
            fetchComments();
            commentTextRef.current.value = '';
        })
    }

    return (
        <>
            <div className="card">
                <div className="card-header">
                    <div className="card-header-title">Leave a comment</div>
                </div>
                <div className="card-content">
                    <textarea className="textarea" placeholder="Nice play!" ref={commentTextRef}></textarea>
                </div>
                <div className="card-content">
                    <div className="buttons">
                        {!annotating ?
                            <button className="button" onClick={toggleAnnotating}>Annotate</button>
                            :
                            <>
                                <button className="button is-danger" onClick={toggleAnnotating}>Clear</button>
                                {/* <button className="button is-info" onClick={saveAnnotation}>Save</button> */}
                            </>
                        }
                        <button className="button" onClick={postComment}>Post @ {fmtSeconds(curTime)}</button>
                    </div>
                </div>
            </div>
            <div className="card">
                <div className="card-header">
                    <div className="card-header-title">Comments</div>
                </div>
                {comments.map((comment, idx) => {
                    return (
                        <div className="card-content" key={idx}>
                            <div className="columns">
                                <div className="column is-one-fifth">
                                    <div className="button is-small"
                                        onClick={() => showComment(comment)}
                                    >
                                        {fmtSeconds(comment.timestamp) + (comment.annotation ? ' ✏️' : '')}
                                    </div>
                                </div>
                                <div className="column">
                                    {comment.text}
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>
        </>
    )
});

export default CommentSection
