

import matplotlib.pyplot as plt
import json


# plt.plot([1,2,3], [4,5,2])
# plt.show()
print("hi")

with open('results.json') as f:
    j = json.load(f)
    # content = f.read()


burst_vals = []
urls = []
reps = []

results = {}

for n_replicas, j2 in j.items():
    n_replicas = int(n_replicas)
    # clips = []
    # clips3 = []
    results[n_replicas] = {}
    for url, j3 in j2.items():
        results[n_replicas][url] = []
        # times = []
        for burstSize, ms in j3.items():
            burstSize = int(burstSize)
            if (n_replicas not in reps):
                reps.append(n_replicas)

            if (url not in urls):
                urls.append(url)

            if (burstSize not in burst_vals):
                burst_vals.append(burstSize)

            # results[n_replicas][url][burstSize] = ms
            results[n_replicas][url].append(ms)


            # times.append(ms)
            # print(n_replicas, url, burstSize, ms)

class URLS:
    clips = 'http://localhost/api/clips/'
    clips3 = 'http://localhost/api/clips/3/'
    clips_by_video = 'http://localhost/api/clips_by_video/3/'
    tags = 'http://localhost/api/tags/'
    tags3 = 'http://localhost/api/tags/3/'
    tag_groups = 'http://localhost/api/tag_groups/'
    tag_groups3 = 'http://localhost/api/tag_groups/3/'


# all_endpoints = [
#     URLS.clips,
#     URLS.clips3,
#     URLS.clips_by_video,
#     URLS.tags,
#     URLS.tags3,
#     URLS.tag_groups,
#     URLS.tag_groups3,
# ]

# First. Fix the burst_size. For each url, calculate resp time for each n_replicas, relative to n_replicas=1
# Then, take the relative val vector for each url and average them.
results_relative = {} # same structure as results, but relative values
results_avg = {}
# Initialize results_avg
for n_replicas in reps:
    results_relative[n_replicas] = {}
    results_avg[n_replicas] = []
    for url in urls:
        results_relative[n_replicas][url] = [None for _ in burst_vals]
        # results_avg[n_replicas][url] = []


# Calculate
for burstSizeIdx in range(len(burst_vals)):
    for url in urls:
        if (burstSizeIdx >= len(results[1][url])):
            continue
        
        time_1rep = results[1][url][burstSizeIdx]
        for n_rep in reps:
            results_relative[n_rep][url][burstSizeIdx] = results[n_rep][url][burstSizeIdx] / time_1rep

    for n_rep in reps:
        total_rel = 0
        num = 0
        for url in urls:
            
            if (burstSizeIdx >= len(results_relative[n_rep][url])):
                continue
            if (results_relative[n_rep][url][burstSizeIdx] is None):
                continue

            num += 1
            total_rel += results_relative[n_rep][url][burstSizeIdx]
        # results_avg[n_rep][burstSizeIdx] = total_rel / num
        results_avg[n_rep].append(total_rel / num)
        
        # relative_time = results[n_rep][url][burstSize]
    
        # results[n_replicas][url][burstSize] = ms
        # results[n_replicas][url].append(ms)



def plot_avg():
    plt.figure(figsize=(4,4))
    # plt.title(f"Average Endpoint")
    plt.title(f"b)")

    for burstSize in [1, 3, 10, 100, 200]:
        y_vals = []
        x_vals = []
        
        burst_idx = burst_vals.index(burstSize)
        for n_reps in reps:    
            if burst_idx >= len(results_avg[n_reps]):
                break
            if None == results_avg[n_reps][burst_idx]:
                break
            
            x_vals.append(n_reps)
            y_vals.append(results_avg[n_reps][burst_idx])
        
        plt.plot(x_vals, y_vals, label=f"Burst Size={burstSize}", marker=".")

    plt.ylabel("Response time, relative to instances=1")
    plt.xlabel("Number of Instances")
    plt.xticks(range(1,11))
    plt.legend(loc="upper center")
    # plt.legend(loc="center")
    # plt.show()
    plt.savefig("F_avg.png", dpi=300, bbox_inches='tight')
    plt.close()

plot_avg()
print(results_avg[10][burst_vals.index(200)])



def plot_relative():
    url=URLS.tag_groups3
    burstSize=50
    plt.figure(figsize=(4,4))
    # plt.title(f"burstSize={burstSize}")
    plt.title("a)")


    
    for url in urls:
        y_vals = []
        x_vals = []
        burst_idx = burst_vals.index(burstSize)
        for n_reps in reps:    
            if burst_idx >= len(results_relative[n_reps][url]):
                continue
            if None == results_relative[n_reps][url][burst_idx]:
                continue
            
            x_vals.append(n_reps)
            y_vals.append(results_relative[n_reps][url][burst_idx])
        
        plt.plot(x_vals, y_vals, label=f"Endpoint: {url[20:]}")

    plt.ylabel("Response time, relative to instances=1")
    plt.xlabel("Number of Instances")
    plt.xticks(range(1,11))
    plt.legend()
    plt.savefig("F_rel.png", dpi=300, bbox_inches='tight')
    plt.close()
    # plt.show()

plot_relative()








def plot_endpoints(n_reps):
    plt.figure()
    plt.title(f"{n_reps} replicas, /api/clips/3/")

    # y_vals = results[n_reps][URLS.clips]
    # x_vals = burst_vals[:len(y_vals)]
    # plt.plot(x_vals, y_vals, label="Clips", marker='o')

    y_vals = results[n_reps][URLS.clips3]
    x_vals = burst_vals[:len(y_vals)]
    plt.plot(x_vals, y_vals, label="Clips3", marker='o')

    plt.ylabel("Average Response Time (ms)")
    plt.xlabel("Burst Size")
    # plt.legend()
    plt.show()

# plot_endpoints(1)
# plot_endpoints(2)
# plot_endpoints(3)
# plot_endpoints(5)


# Plots 
def plot_F1():
    plt.figure(figsize=(4,3))
    # plt.title(f"Average Response Time vs Burst Size\n (instances=1, endpoint='/clips/3/')")

    # y_vals = results[n_reps][URLS.clips]
    # x_vals = burst_vals[:len(y_vals)]
    # plt.plot(x_vals, y_vals, label="Clips", marker='o')

    n_reps = 1
    y_vals = results[n_reps][URLS.clips3]
    x_vals = burst_vals[:len(y_vals)]
    plt.plot(x_vals, y_vals, label="Clips3", marker='o')

    plt.ylabel("Average Response Time (ms)")
    plt.xlabel("Burst Size")
    # plt.legend()
    plt.savefig("F1.png", dpi=300, bbox_inches='tight')
    plt.close()
    # plt.show()

    # print(urls)
    # print(results)

plot_F1()


def plot_replicas(url):
    plt.figure()
    plt.title(f"URL: {url}")
    print("reps:", reps)

    for n_reps in reps:
        y0 = results[n_reps][url]
        y_vals = results[n_reps][url]
        x_vals = burst_vals[:len(y_vals)]
        plt.plot(x_vals, y_vals, label=f"{n_reps} replicas", marker='o')


    plt.ylabel("ms")
    plt.xlabel("Burst Size")
    plt.legend()
    plt.show()



# plot_replicas(URLS.clips)
# plot_replicas(URLS.clips3)


# clips/3, with # replicas on x axis
def plot3(burstSize, url):
    plt.figure()
    plt.title(f"burstSize={burstSize}, URL={url}")

    y_vals = []
    x_vals = []
    
    burst_idx = burst_vals.index(burstSize)
    for n_reps in reps:    
        if burst_idx >= len(results[n_reps][url]):
            break
        
        x_vals.append(n_reps)
        y_vals.append(results[n_reps][url][burst_idx])
    
    plt.plot(x_vals, y_vals)

    plt.ylabel("ms")
    plt.xlabel("Number of Replicas")
    # plt.legend()
    plt.show()

# print(burst_vals)
# plot3(100, URLS.clips3)
# plot3(150, URLS.clips3)
# plot3(200, URLS.clips3)

# like plot3(), but multiple values:
def plot4(burstSizes, url):
    plt.figure()
    plt.title(f"burstSize={burstSizes}, URL={url}")

    for burstSize in burstSizes:
        y_vals = []
        x_vals = []
        burst_idx = burst_vals.index(burstSize)
        for n_reps in reps:    
            if burst_idx >= len(results[n_reps][url]):
                break
            
            x_vals.append(n_reps)
            y_vals.append(results[n_reps][url][burst_idx])
        
        plt.plot(x_vals, y_vals, label=f"Burst size: {burstSize}")

    plt.ylabel("ms")
    plt.xlabel("Number of Replicas")
    plt.legend()
    # plt.show()

# # plot4([1, 25, 50, 100, 150, 200], URLS.clips)
# plot4([1, 25, 50, 100, 150, 200], URLS.clips3)
# # plot4([1, 25, 50, 100, 150, 200], URLS.clips_by_video)
# # plot4([1, 25, 50, 100, 150, 200], URLS.tags)
# # plot4([1, 25, 50, 100, 150, 200], URLS.tags3)
# plot4([1, 25, 50, 100, 150, 200], URLS.tag_groups)
# plot4([1, 5, 10, 25, 50], URLS.clips)
# # plot4([1, 25, 50, 100, 150, 200], URLS.tag_groups3)
# plt.show()



# Bar graph of each endpoint performance
# Bar plot, each endpoint, instances=1, burstsize=1
def plot5():
    x_vals = []
    y_vals = []
    for url in urls:
        x_vals.append(url)
        n_replicas=1
        burst_size=1
        y_vals.append(results[n_replicas][url][burst_size])
    plt.bar(x_vals, y_vals)
    plt.show()

# plot5()


# clips = 'http://localhost/api/clips/'
# clips3 = 'http://localhost/api/clips/3/'
# clips_by_video = 'http://localhost/api/clips_by_video/3/'
# tags = 'http://localhost/api/tags/'
# tags3 = 'http://localhost/api/tags/3/'
# tag_groups = 'http://localhost/api/tag_groups/'
# tag_groups3 = 'http://localhost/api/tag_groups/3/'