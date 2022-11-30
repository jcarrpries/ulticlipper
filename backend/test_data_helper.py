# Load this shortened example data CSV in memory so unit tests don't have to access disk

CSV_STRING = b'''Date/Time,Tournamemnt,Opponent,Point Elapsed Seconds,Line,Our Score - End of Point,Their Score - End of Point,Event Type,Action,Passer,Receiver,Defender,Hang Time (secs),Player 0,Player 1,Player 2,Player 3,Player 4,Player 5,Player 6,Player 7,Player 8,Player 9,Player 10,Player 11,Player 12,Player 13,Player 14,Player 15,Player 16,Player 17,Player 18,Player 19,Player 20,Player 21,Player 22,Player 23,Player 24,Player 25,Player 26,Player 27,Elapsed Time (secs),Begin Area,Begin X,Begin Y,End Area,End X,End Y,Distance Unit of Measure,Absolute Distance,Lateral Distance,Toward Our Goal Distance
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,LavioleA,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,0
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,13
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,17
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,21
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,25
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,29
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,33
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,Anonymous,FreystaM,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,37
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,41
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,45
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,FairfaxJ,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,49
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,LeyBobby,MitchelT,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,53
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,MitchelT,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,57
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,LeyBobby,FisherHe,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,61
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,FisherHe,FreystaM,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,65
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Catch,FreystaM,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,69
2019-06-22 19:03,AUDL,New York Empire,75,O,1,0,Offense,Goal,TaylorEr,FisherHe,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,73
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Defense,Pull,,,AllenJus,5.322,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,96
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Defense,Throwaway,,,Anonymous,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,116
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,187
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,191
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,195
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,199
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,203
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,207
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,211
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,215
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,219
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,223
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,227
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Catch,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,231
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Offense,Throwaway,Anonymous,Anonymous,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,235
2019-06-22 19:03,AUDL,New York Empire,182,D,1,1,Defense,Goal,,,Anonymous,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,276
2019-06-22 19:03,AUDL,New York Empire,21,O,2,1,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,,,,,,,,,,,,,,,,,,,,,,327
2019-06-22 19:03,AUDL,New York Empire,21,O,2,1,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,,,,,,,,,,,,,,,,,,,,,,337
2019-06-22 19:03,AUDL,New York Empire,21,O,2,1,Offense,Catch,FairfaxJ,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,,,,,,,,,,,,,,,,,,,,,,341
2019-06-22 19:03,AUDL,New York Empire,21,O,2,1,Offense,Goal,LeyBobby,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,,,,,,,,,,,,,,,,,,,,,,346
2019-06-22 19:03,AUDL,New York Empire,28,D,2,2,Defense,Pull,,,McAllisT,6.023,FairfaxJ,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,403
2019-06-22 19:03,AUDL,New York Empire,28,D,2,2,Defense,Goal,,,Anonymous,,FairfaxJ,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,429
2019-06-22 19:03,AUDL,New York Empire,34,O,2,3,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,581
2019-06-22 19:03,AUDL,New York Empire,34,O,2,3,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,590
2019-06-22 19:03,AUDL,New York Empire,34,O,2,3,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,594
2019-06-22 19:03,AUDL,New York Empire,34,O,2,3,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,598
2019-06-22 19:03,AUDL,New York Empire,34,O,2,3,Offense,Throwaway,LeyBobby,Anonymous,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,603
2019-06-22 19:03,AUDL,New York Empire,34,O,2,3,Defense,Goal,,,Anonymous,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,613
2019-06-22 19:03,AUDL,New York Empire,28,O,3,3,Offense,Catch,LavioleA,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,676
2019-06-22 19:03,AUDL,New York Empire,28,O,3,3,Offense,Catch,LeyBobby,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,685
2019-06-22 19:03,AUDL,New York Empire,28,O,3,3,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,689
2019-06-22 19:03,AUDL,New York Empire,28,O,3,3,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,693
2019-06-22 19:03,AUDL,New York Empire,28,O,3,3,Offense,Catch,FairfaxJ,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,697
2019-06-22 19:03,AUDL,New York Empire,28,O,3,3,Offense,Goal,TaylorEr,FisherHe,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,702
2019-06-22 19:03,AUDL,New York Empire,51,D,3,4,Defense,Pull,,,AllenJus,5.706,HastingJ,AllenJus,CantoneC,PannoneM,YanuckSo,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,772
2019-06-22 19:03,AUDL,New York Empire,51,D,3,4,Defense,Goal,,,Anonymous,,HastingJ,AllenJus,CantoneC,PannoneM,YanuckSo,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,821
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,871
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,880
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,884
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,888
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,892
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,AllenKir,FisherHe,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,896
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,900
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,904
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,908
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,912
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Offense,Drop,FairfaxJ,LavioleA,,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,920
2019-06-22 19:03,AUDL,New York Empire,211,O,3,5,Defense,Goal,,,Anonymous,,FairfaxJ,HastingJ,AllenJus,FisherHe,RichardD,YanuckSo,WardRoss,McAllisT,LavioleA,TaylorEr,AllenKir,LeyBobby,FreystaM,,,,,,,,,,,,,,,,1080
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1236
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1246
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1250
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1253
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1258
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1264
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,FairfaxJ,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1268
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,LeyBobby,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1274
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,LavioleA,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1278
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,LeyBobby,FisherHe,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1282
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,FisherHe,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1286
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1290
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,TaylorEr,MitchelT,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1294
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1300
2019-06-22 19:03,AUDL,New York Empire,72,O,4,5,Offense,Goal,FreystaM,FairfaxJ,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1306
2019-06-22 19:03,AUDL,New York Empire,67,D,4,6,Defense,Pull,,,McAllisT,3.275,HastingJ,AllenJus,McKelveA,RichardD,YanuckSo,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,1365
2019-06-22 19:03,AUDL,New York Empire,67,D,4,6,Defense,Goal,,,Anonymous,,HastingJ,AllenJus,McKelveA,RichardD,YanuckSo,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,1430
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1487
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1495
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Catch,FreystaM,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1500
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Catch,MitchelT,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1506
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1510
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1514
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Catch,FreystaM,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1518
2019-06-22 19:03,AUDL,New York Empire,37,O,5,6,Offense,Goal,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1522
2019-06-22 19:03,AUDL,New York Empire,29,D,5,7,Defense,Pull,,,CantoneC,2.373,CantoneC,PannoneM,WardRoss,RussellC,FreystaM,McAllisT,LavioleA,,,,,,,,,,,,,,,,,,,,,,1578
2019-06-22 19:03,AUDL,New York Empire,29,D,5,7,Defense,Goal,,,Anonymous,,CantoneC,PannoneM,WardRoss,RussellC,FreystaM,McAllisT,LavioleA,,,,,,,,,,,,,,,,,,,,,,1605
2019-06-22 19:03,AUDL,New York Empire,7,O,5,7,Cessation,EndOfFirstQuarter,,,,,FairfaxJ,MouwJaco,LeyBobby,AllenJus,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1666
2019-06-22 19:03,AUDL,New York Empire,43,D,5,8,Defense,Pull,,,AllenJus,1.592,AllenJus,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,1890
2019-06-22 19:03,AUDL,New York Empire,43,D,5,8,Defense,Goal,,,Anonymous,,AllenJus,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,1931
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1981
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1993
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Catch,LeyBobby,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1997
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Catch,LavioleA,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2001
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2005
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Catch,TaylorEr,MitchelT,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2009
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2013
2019-06-22 19:03,AUDL,New York Empire,38,O,6,8,Offense,Goal,FreystaM,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2017
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Defense,Pull,,,AllenJus,8.575,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2071
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Defense,D,,,McAllisT,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2084
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2200
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Catch,LeyBobby,MitchelT,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2204
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Catch,MitchelT,LeyBobby,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2209
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2218
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2221
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2224
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Catch,LeyBobby,LavioleA,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2229
2019-06-22 19:03,AUDL,New York Empire,163,D,7,8,Offense,Goal,LavioleA,FisherHe,,,FairfaxJ,HastingJ,FisherHe,AllenJus,YanuckSo,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,2232
2019-06-22 19:03,AUDL,New York Empire,29,D,7,9,Defense,Pull,,,McAllisT,7.827,HastingJ,CantoneC,RichardD,PannoneM,YanuckSo,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,2296
2019-06-22 19:03,AUDL,New York Empire,29,D,7,9,Defense,Goal,,,Anonymous,,HastingJ,CantoneC,RichardD,PannoneM,YanuckSo,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,2323
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2386
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,LavioleA,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2394
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2398
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2402
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2406
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2410
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,LeyBobby,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2414
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,AllenKir,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2418
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,MitchelT,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2422
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2426
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,TaylorEr,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2430
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Catch,MitchelT,LavioleA,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2434
2019-06-22 19:03,AUDL,New York Empire,53,O,8,9,Offense,Goal,LavioleA,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2437
2019-06-22 19:03,AUDL,New York Empire,70,D,8,10,Defense,Pull,,,AllenJus,7.113,HastingJ,AllenJus,McKelveA,YanuckSo,FreystaM,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,2608
2019-06-22 19:03,AUDL,New York Empire,70,D,8,10,Defense,Throwaway,,,Anonymous,,HastingJ,AllenJus,McKelveA,YanuckSo,FreystaM,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,2627
2019-06-22 19:03,AUDL,New York Empire,70,D,8,10,Offense,Catch,YanuckSo,GreenTri,,,HastingJ,AllenJus,McKelveA,YanuckSo,FreystaM,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,2638
2019-06-22 19:03,AUDL,New York Empire,70,D,8,10,Offense,Throwaway,GreenTri,Anonymous,,,HastingJ,AllenJus,McKelveA,YanuckSo,FreystaM,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,2644
2019-06-22 19:03,AUDL,New York Empire,70,D,8,10,Defense,Goal,,,Anonymous,,HastingJ,AllenJus,McKelveA,YanuckSo,FreystaM,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,2676
2019-06-22 19:03,AUDL,New York Empire,24,O,9,10,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2724
2019-06-22 19:03,AUDL,New York Empire,24,O,9,10,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2732
2019-06-22 19:03,AUDL,New York Empire,24,O,9,10,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2736
2019-06-22 19:03,AUDL,New York Empire,24,O,9,10,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2740
2019-06-22 19:03,AUDL,New York Empire,24,O,9,10,Offense,Goal,LeyBobby,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2746
2019-06-22 19:03,AUDL,New York Empire,57,D,9,11,Defense,Pull,,,McAllisT,7.729,MouwJaco,RichardD,PannoneM,WardRoss,RussellC,McAllisT,LavioleA,,,,,,,,,,,,,,,,,,,,,,2807
2019-06-22 19:03,AUDL,New York Empire,57,D,9,11,Defense,Goal,,,Anonymous,,MouwJaco,RichardD,PannoneM,WardRoss,RussellC,McAllisT,LavioleA,,,,,,,,,,,,,,,,,,,,,,2862
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2940
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2949
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2953
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2957
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2961
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Catch,FairfaxJ,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2965
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2969
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Offense,Drop,FreystaM,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2986
2019-06-22 19:03,AUDL,New York Empire,88,O,9,12,Defense,Goal,,,Anonymous,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3026
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,YanuckSo,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3176
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3184
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,LavioleA,FisherHe,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3188
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3192
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3198
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,LavioleA,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3202
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3207
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3211
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Catch,LavioleA,YanuckSo,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3215
2019-06-22 19:03,AUDL,New York Empire,45,O,10,12,Offense,Goal,YanuckSo,MitchelT,,,FairfaxJ,LeyBobby,FisherHe,YanuckSo,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3219
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Defense,Pull,,,AllenJus,6.884,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3276
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Defense,Throwaway,,,Anonymous,,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3347
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3459
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Offense,Catch,FreystaM,FisherHe,,,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3463
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Offense,Catch,FisherHe,FreystaM,,,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3467
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Offense,Catch,FreystaM,MitchelT,,,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3471
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Offense,Catch,MitchelT,LeyBobby,,,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3475
2019-06-22 19:03,AUDL,New York Empire,205,D,11,12,Offense,Goal,LeyBobby,TaylorEr,,,FairfaxJ,HastingJ,FisherHe,AllenJus,RichardD,LavioleA,McAllisT,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,FreystaM,GreenTri,,,,,,,,,,,,,,,3479
2019-06-22 19:03,AUDL,New York Empire,76,D,11,12,Defense,PullOb,,,AllenJus,,AllenJus,RichardD,PannoneM,YanuckSo,WardRoss,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,3577
2019-06-22 19:03,AUDL,New York Empire,76,D,11,12,Defense,Throwaway,,,Anonymous,,AllenJus,RichardD,PannoneM,YanuckSo,WardRoss,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,3647
2019-06-22 19:03,AUDL,New York Empire,76,D,11,12,Cessation,Halftime,,,,,AllenJus,RichardD,PannoneM,YanuckSo,WardRoss,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,3651
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4540
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4550
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,FreystaM,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4554
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,FisherHe,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4558
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4562
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,FreystaM,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4566
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4572
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Catch,FisherHe,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4576
2019-06-22 19:03,AUDL,New York Empire,42,O,12,12,Offense,Goal,FairfaxJ,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4580
2019-06-22 19:03,AUDL,New York Empire,56,D,12,13,Defense,PullOb,,,AllenJus,,AllenJus,PannoneM,YanuckSo,WardRoss,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,4634
2019-06-22 19:03,AUDL,New York Empire,56,D,12,13,Defense,Goal,,,Anonymous,,AllenJus,PannoneM,YanuckSo,WardRoss,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,4688
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4743
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4753
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4757
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,LeyBobby,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4761
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4765
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,LeyBobby,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4769
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,FisherHe,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4773
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,MitchelT,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4777
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4781
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,FreystaM,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4785
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4789
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,AllenKir,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4793
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,MitchelT,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4797
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4801
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4805
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4809
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4813
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4817
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4821
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4825
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4829
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4833
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4837
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4841
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4845
2019-06-22 19:03,AUDL,New York Empire,108,O,13,13,Offense,Goal,LeyBobby,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4849
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Defense,Pull,,,CantoneC,6.508,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4878
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Defense,D,,,McKelveA,,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4918
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Offense,Catch,YanuckSo,HastingJ,,,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4929
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Offense,Catch,HastingJ,YanuckSo,,,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4935
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Offense,Catch,YanuckSo,HastingJ,,,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4939
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Offense,Catch,HastingJ,LavioleA,,,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4943
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Offense,Throwaway,LavioleA,Anonymous,,,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4946
2019-06-22 19:03,AUDL,New York Empire,115,D,13,14,Defense,Goal,,,Anonymous,,HastingJ,CantoneC,McKelveA,RichardD,YanuckSo,RussellC,LavioleA,,,,,,,,,,,,,,,,,,,,,,4991
2019-06-22 19:03,AUDL,New York Empire,32,O,14,14,Offense,Catch,Anonymous,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5150
2019-06-22 19:03,AUDL,New York Empire,32,O,14,14,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5162
2019-06-22 19:03,AUDL,New York Empire,32,O,14,14,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5166
2019-06-22 19:03,AUDL,New York Empire,32,O,14,14,Offense,Catch,TaylorEr,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5170
2019-06-22 19:03,AUDL,New York Empire,32,O,14,14,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5173
2019-06-22 19:03,AUDL,New York Empire,32,O,14,14,Offense,Goal,FreystaM,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5180
2019-06-22 19:03,AUDL,New York Empire,15,D,14,15,Defense,Pull,,,AllenJus,5.002,AllenJus,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,5248
2019-06-22 19:03,AUDL,New York Empire,15,D,14,15,Defense,Goal,,,Anonymous,,AllenJus,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,5261
2019-06-22 19:03,AUDL,New York Empire,41,O,15,15,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5315
2019-06-22 19:03,AUDL,New York Empire,41,O,15,15,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5326
2019-06-22 19:03,AUDL,New York Empire,41,O,15,15,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5330
2019-06-22 19:03,AUDL,New York Empire,41,O,15,15,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5333
2019-06-22 19:03,AUDL,New York Empire,41,O,15,15,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5337
2019-06-22 19:03,AUDL,New York Empire,41,O,15,15,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5340
2019-06-22 19:03,AUDL,New York Empire,41,O,15,15,Offense,Goal,LeyBobby,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5354
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Defense,Pull,,,CantoneC,5.513,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5403
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Defense,D,,,LavioleA,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5412
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,YanuckSo,HastingJ,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5431
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,HastingJ,McKelveA,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5435
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,McKelveA,LavioleA,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5439
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,LavioleA,PannoneM,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5443
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,PannoneM,LavioleA,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5447
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,LavioleA,HastingJ,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5451
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,HastingJ,RussellC,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5455
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5557
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,LeyBobby,LavioleA,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5565
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Catch,LavioleA,FreystaM,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5568
2019-06-22 19:03,AUDL,New York Empire,175,D,16,15,Offense,Goal,FreystaM,FisherHe,,,FairfaxJ,HastingJ,FisherHe,PannoneM,YanuckSo,LavioleA,MitchelT,TaylorEr,LeyBobby,CantoneC,McKelveA,RussellC,FreystaM,,,,,,,,,,,,,,,,5576
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Defense,Pull,,,McAllisT,7.352,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5755
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Defense,Throwaway,,,Anonymous,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5846
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,YanuckSo,GreenTri,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5859
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,GreenTri,McAllisT,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5867
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,McAllisT,GreenTri,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5876
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,GreenTri,WardRoss,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5879
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,WardRoss,GreenTri,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5882
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,GreenTri,YanuckSo,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5885
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,YanuckSo,WardRoss,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5894
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,WardRoss,YanuckSo,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5898
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,YanuckSo,HastingJ,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5902
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Catch,HastingJ,GreenTri,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5906
2019-06-22 19:03,AUDL,New York Empire,157,D,17,15,Offense,Goal,GreenTri,CantoneC,,,HastingJ,AllenJus,CantoneC,RichardD,YanuckSo,WardRoss,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,5910
2019-06-22 19:03,AUDL,New York Empire,40,D,17,16,Defense,Pull,,,FairfaxJ,6.768,FairfaxJ,MouwJaco,CantoneC,McKelveA,PannoneM,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5971
2019-06-22 19:03,AUDL,New York Empire,40,D,17,16,Defense,Goal,,,Anonymous,,FairfaxJ,MouwJaco,CantoneC,McKelveA,PannoneM,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6009
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,LeyBobby,FisherHe,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6078
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,FisherHe,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6086
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6089
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,FreystaM,LavioleA,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6093
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,LavioleA,FreystaM,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6097
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,FreystaM,FairfaxJ,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6111
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,FairfaxJ,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6121
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6125
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6129
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,FairfaxJ,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6133
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,LeyBobby,FisherHe,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6138
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,FisherHe,LeyBobby,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6142
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6145
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Catch,FairfaxJ,TaylorEr,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6150
2019-06-22 19:03,AUDL,New York Empire,84,O,18,16,Offense,Goal,TaylorEr,MitchelT,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6160
2019-06-22 19:03,AUDL,New York Empire,19,D,18,16,Defense,Pull,,,TaylorEr,3.578,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6223
2019-06-22 19:03,AUDL,New York Empire,19,D,18,16,Defense,D,,,FairfaxJ,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6235
2019-06-22 19:03,AUDL,New York Empire,19,D,18,16,Cessation,EndOfThirdQuarter,,,,,FairfaxJ,LeyBobby,FisherHe,FreystaM,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6240
2019-06-22 19:03,AUDL,New York Empire,64,D,18,17,Defense,Pull,,,McAllisT,,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,6449
2019-06-22 19:03,AUDL,New York Empire,64,D,18,17,Defense,D,,,RichardD,,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,6455
2019-06-22 19:03,AUDL,New York Empire,64,D,18,17,Offense,Catch,GreenTri,YanuckSo,,,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,6464
2019-06-22 19:03,AUDL,New York Empire,64,D,18,17,Offense,Catch,YanuckSo,McAllisT,,,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,6467
2019-06-22 19:03,AUDL,New York Empire,64,D,18,17,Offense,Catch,McAllisT,RussellC,,,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,6470
2019-06-22 19:03,AUDL,New York Empire,64,D,18,17,Offense,Throwaway,RussellC,Anonymous,,,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,6479
2019-06-22 19:03,AUDL,New York Empire,64,D,18,17,Defense,Goal,,,Anonymous,,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,GreenTri,,,,,,,,,,,,,,,,,,,,,,6511
2019-06-22 19:03,AUDL,New York Empire,24,O,19,17,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6566
2019-06-22 19:03,AUDL,New York Empire,24,O,19,17,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6576
2019-06-22 19:03,AUDL,New York Empire,24,O,19,17,Offense,Goal,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6588
2019-06-22 19:03,AUDL,New York Empire,67,D,19,18,Defense,PullOb,,,McAllisT,,HastingJ,McKelveA,PannoneM,YanuckSo,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,6650
2019-06-22 19:03,AUDL,New York Empire,67,D,19,18,Defense,Goal,,,Anonymous,,HastingJ,McKelveA,PannoneM,YanuckSo,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,6715
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6775
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6786
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6789
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6793
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6798
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Catch,FisherHe,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6802
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Catch,FreystaM,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6806
2019-06-22 19:03,AUDL,New York Empire,39,O,20,18,Offense,Goal,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6812
2019-06-22 19:03,AUDL,New York Empire,53,D,20,19,Defense,Pull,,,CantoneC,7.638,HastingJ,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,6873
2019-06-22 19:03,AUDL,New York Empire,53,D,20,19,Defense,Goal,,,Anonymous,,HastingJ,CantoneC,RichardD,YanuckSo,WardRoss,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,6924
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7074
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,AllenKir,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7084
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7087
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7090
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7093
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7098
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,FisherHe,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7102
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7106
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7110
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7114
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,LeyBobby,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7118
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,MitchelT,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7122
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7126
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Catch,FairfaxJ,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7130
2019-06-22 19:03,AUDL,New York Empire,68,O,21,19,Offense,Goal,MitchelT,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7140
2019-06-22 19:03,AUDL,New York Empire,90,D,21,20,Defense,Pull,,,McAllisT,6.919,RichardD,PannoneM,YanuckSo,RussellC,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,7196
2019-06-22 19:03,AUDL,New York Empire,90,D,21,20,Defense,Goal,,,Anonymous,,RichardD,PannoneM,YanuckSo,RussellC,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,7284
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7348
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,LeyBobby,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7357
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7360
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,LeyBobby,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7364
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,FisherHe,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7368
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7371
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,TaylorEr,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7374
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7377
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,FreystaM,FisherHe,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7382
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,FisherHe,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7386
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7397
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7419
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7423
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,FreystaM,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7427
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Catch,TaylorEr,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7431
2019-06-22 19:03,AUDL,New York Empire,89,O,22,20,Offense,Goal,MitchelT,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7435
2019-06-22 19:03,AUDL,New York Empire,42,D,22,21,Defense,Pull,,,McAllisT,,HastingJ,MouwJaco,CantoneC,McKelveA,YanuckSo,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,7610
2019-06-22 19:03,AUDL,New York Empire,42,D,22,21,Defense,Goal,,,Anonymous,,HastingJ,MouwJaco,CantoneC,McKelveA,YanuckSo,RussellC,McAllisT,,,,,,,,,,,,,,,,,,,,,,7650
2019-06-22 19:03,AUDL,New York Empire,32,O,23,21,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7787
2019-06-22 19:03,AUDL,New York Empire,32,O,23,21,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7796
2019-06-22 19:03,AUDL,New York Empire,32,O,23,21,Offense,Catch,FisherHe,FairfaxJ,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7805
2019-06-22 19:03,AUDL,New York Empire,32,O,23,21,Offense,Catch,FairfaxJ,FreystaM,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7809
2019-06-22 19:03,AUDL,New York Empire,32,O,23,21,Offense,Catch,FreystaM,FairfaxJ,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7813
2019-06-22 19:03,AUDL,New York Empire,32,O,23,21,Offense,Goal,FairfaxJ,MitchelT,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7817
2019-06-22 19:03,AUDL,New York Empire,19,D,23,22,Defense,Pull,,,LavioleA,5.403,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,7875
2019-06-22 19:03,AUDL,New York Empire,19,D,23,22,Defense,Goal,,,Anonymous,,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,7892
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7957
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,AllenKir,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7966
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,FairfaxJ,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7973
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7976
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,FairfaxJ,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7981
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7987
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7990
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7993
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,7998
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Catch,FreystaM,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8002
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Offense,Throwaway,TaylorEr,Anonymous,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8006
2019-06-22 19:03,AUDL,New York Empire,167,O,23,23,Defense,Goal,,,Anonymous,,FairfaxJ,AllenKir,LeyBobby,FisherHe,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,GreenTri,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8122
2019-06-22 19:03,AUDL,New York Empire,183,O,23,23,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,MouwJaco,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8264
2019-06-22 19:03,AUDL,New York Empire,183,O,23,23,Offense,Catch,LeyBobby,FairfaxJ,,,FairfaxJ,MouwJaco,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8273
2019-06-22 19:03,AUDL,New York Empire,183,O,23,23,Cessation,EndOfFourthQuarter,,,,,FairfaxJ,MouwJaco,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8445
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,TaylorEr,LeyBobby,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8592
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,LeyBobby,FreystaM,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8604
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,FreystaM,LeyBobby,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8608
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,LeyBobby,FisherHe,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8611
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,FisherHe,TaylorEr,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8614
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,TaylorEr,FairfaxJ,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8618
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,FairfaxJ,LavioleA,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8624
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,LavioleA,LeyBobby,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8628
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,LeyBobby,FairfaxJ,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8631
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,FairfaxJ,LeyBobby,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8634
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,LeyBobby,LavioleA,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8652
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,LavioleA,LeyBobby,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8657
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,LeyBobby,TaylorEr,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8661
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,TaylorEr,FreystaM,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8664
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,FreystaM,FairfaxJ,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8668
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,FairfaxJ,TaylorEr,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8671
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,TaylorEr,FreystaM,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8675
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Catch,FreystaM,TaylorEr,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8679
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Offense,Throwaway,TaylorEr,Anonymous,,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8684
2019-06-22 19:03,AUDL,New York Empire,255,O,23,24,Defense,Goal,,,Anonymous,,HastingJ,FairfaxJ,LeyBobby,FisherHe,CantoneC,RichardD,YanuckSo,McAllisT,LavioleA,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,8845
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8902
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8910
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8913
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,LeyBobby,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8917
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,AllenKir,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8921
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8925
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8929
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8933
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8937
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8940
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8944
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,8952
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9000
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9003
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,LeyBobby,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9008
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,FreystaM,MitchelT,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9014
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9018
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Catch,FreystaM,LeyBobby,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9022
2019-06-22 19:03,AUDL,New York Empire,129,O,24,24,Offense,Goal,LeyBobby,FairfaxJ,,,FairfaxJ,AllenKir,LeyBobby,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,9029
2019-06-22 19:03,AUDL,New York Empire,119,D,24,24,Defense,Pull,,,McAllisT,2.095,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,9087
2019-06-22 19:03,AUDL,New York Empire,119,D,24,24,Defense,D,,,RichardD,,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,9123
2019-06-22 19:03,AUDL,New York Empire,119,D,24,24,Cessation,EndOfOvertime,,,,,RichardD,PannoneM,YanuckSo,WardRoss,McAllisT,LavioleA,GreenTri,,,,,,,,,,,,,,,,,,,,,,9204
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Defense,Pull,,,TaylorEr,7.582,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9285
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Defense,Throwaway,,,Anonymous,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9458
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,TaylorEr,LeyBobby,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9464
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,LeyBobby,MitchelT,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9468
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,MitchelT,LeyBobby,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9472
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,LeyBobby,MitchelT,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9476
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,MitchelT,LeyBobby,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9480
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,LeyBobby,TaylorEr,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9484
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9488
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,LavioleA,LeyBobby,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9496
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,LeyBobby,LavioleA,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9500
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Catch,LavioleA,LeyBobby,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9504
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Offense,Throwaway,LeyBobby,Anonymous,,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9508
2019-06-22 19:03,AUDL,New York Empire,429,D,24,25,Defense,Goal,,,Anonymous,,FairfaxJ,HastingJ,LeyBobby,FisherHe,RichardD,YanuckSo,FreystaM,McAllisT,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,9712
2019-06-22 19:03,AUDL,New York Empire,7,O,24,25,Cessation,GameOver,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,9711
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,0
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,TaylorEr,MunizCha,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,10
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,MunizCha,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,13
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,FisherHe,MitchelT,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,19
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Drop,MitchelT,AllenKir,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,22
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Defense,Throwaway,,,Anonymous,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,88
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,TaylorEr,MunizCha,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,105
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,MunizCha,AllenKir,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,109
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,AllenKir,FairfaxJ,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,113
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Catch,FairfaxJ,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,117
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Offense,Throwaway,TaylorEr,Anonymous,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,121
2019-04-05 19:24,AUDL,Dallas Roughnecks,156,O,0,1,Defense,Goal,,,Anonymous,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,154
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,SaulNoah,MouwJaco,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,241
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,MouwJaco,SaulNoah,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,258
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,SaulNoah,McKelveA,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,265
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Throwaway,McKelveA,Anonymous,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,272
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Defense,Throwaway,,,Anonymous,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,304
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,TaylorEr,McAllisT,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,308
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,McAllisT,TaylorEr,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,311
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,TaylorEr,SaulNoah,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,317
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,SaulNoah,FisherHe,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,322
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,FisherHe,SaulNoah,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,326
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Catch,SaulNoah,FreystaM,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,330
2019-04-05 19:24,AUDL,Dallas Roughnecks,95,O,1,1,Offense,Goal,FreystaM,FisherHe,,,SaulNoah,MouwJaco,FisherHe,McKelveA,FreystaM,McAllisT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,334
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,2,1,Defense,Pull,,,HartzogJ,6.961,HastingJ,HartzogJ,RichardD,WardRoss,YanuckSo,PolkJake,LynchJoh,,,,,,,,,,,,,,,,,,,,,,397
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,2,1,Defense,Throwaway,,,Anonymous,,HastingJ,HartzogJ,RichardD,WardRoss,YanuckSo,PolkJake,LynchJoh,,,,,,,,,,,,,,,,,,,,,,401
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,2,1,Offense,Catch,YanuckSo,HastingJ,,,HastingJ,HartzogJ,RichardD,WardRoss,YanuckSo,PolkJake,LynchJoh,,,,,,,,,,,,,,,,,,,,,,411
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,2,1,Offense,Catch,HastingJ,YanuckSo,,,HastingJ,HartzogJ,RichardD,WardRoss,YanuckSo,PolkJake,LynchJoh,,,,,,,,,,,,,,,,,,,,,,414
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,2,1,Offense,Catch,YanuckSo,HartzogJ,,,HastingJ,HartzogJ,RichardD,WardRoss,YanuckSo,PolkJake,LynchJoh,,,,,,,,,,,,,,,,,,,,,,418
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,2,1,Offense,Goal,HartzogJ,RichardD,,,HastingJ,HartzogJ,RichardD,WardRoss,YanuckSo,PolkJake,LynchJoh,,,,,,,,,,,,,,,,,,,,,,421
2019-04-05 19:24,AUDL,Dallas Roughnecks,87,D,3,1,Defense,Pull,,,SaulNoah,5.598,HastingJ,SaulNoah,McKelveA,NordgreJ,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,487
2019-04-05 19:24,AUDL,Dallas Roughnecks,87,D,3,1,Defense,Throwaway,,,Anonymous,,HastingJ,SaulNoah,McKelveA,NordgreJ,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,532
2019-04-05 19:24,AUDL,Dallas Roughnecks,87,D,3,1,Offense,Catch,YanuckSo,FreystaM,,,HastingJ,SaulNoah,McKelveA,NordgreJ,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,535
2019-04-05 19:24,AUDL,Dallas Roughnecks,87,D,3,1,Offense,Catch,FreystaM,NordgreJ,,,HastingJ,SaulNoah,McKelveA,NordgreJ,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,569
2019-04-05 19:24,AUDL,Dallas Roughnecks,87,D,3,1,Offense,Goal,NordgreJ,FreystaM,,,HastingJ,SaulNoah,McKelveA,NordgreJ,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,572
2019-04-05 19:24,AUDL,Dallas Roughnecks,54,D,4,1,Defense,Pull,,,HartzogJ,6.771,FairfaxJ,HartzogJ,WardRoss,PolkJake,LavioleA,MunizCha,LynchJoh,,,,,,,,,,,,,,,,,,,,,,622
2019-04-05 19:24,AUDL,Dallas Roughnecks,54,D,4,1,Defense,Throwaway,,,Anonymous,,FairfaxJ,HartzogJ,WardRoss,PolkJake,LavioleA,MunizCha,LynchJoh,,,,,,,,,,,,,,,,,,,,,,649
2019-04-05 19:24,AUDL,Dallas Roughnecks,54,D,4,1,Offense,Catch,LavioleA,LynchJoh,,,FairfaxJ,HartzogJ,WardRoss,PolkJake,LavioleA,MunizCha,LynchJoh,,,,,,,,,,,,,,,,,,,,,,668
2019-04-05 19:24,AUDL,Dallas Roughnecks,54,D,4,1,Offense,Goal,LynchJoh,HartzogJ,,,FairfaxJ,HartzogJ,WardRoss,PolkJake,LavioleA,MunizCha,LynchJoh,,,,,,,,,,,,,,,,,,,,,,674
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,4,2,Defense,Pull,,,McAllisT,3.6,HastingJ,HartzogJ,RichardD,YanuckSo,FreystaM,McAllisT,MitchelT,,,,,,,,,,,,,,,,,,,,,,740
2019-04-05 19:24,AUDL,Dallas Roughnecks,26,D,4,2,Defense,Goal,,,Anonymous,,HastingJ,HartzogJ,RichardD,YanuckSo,FreystaM,McAllisT,MitchelT,,,,,,,,,,,,,,,,,,,,,,764
2019-04-05 19:24,AUDL,Dallas Roughnecks,20,O,5,2,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,MouwJaco,FisherHe,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,822
2019-04-05 19:24,AUDL,Dallas Roughnecks,20,O,5,2,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,SaulNoah,MouwJaco,FisherHe,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,830
2019-04-05 19:24,AUDL,Dallas Roughnecks,20,O,5,2,Offense,Catch,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,SaulNoah,MouwJaco,FisherHe,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,834
2019-04-05 19:24,AUDL,Dallas Roughnecks,20,O,5,2,Offense,Goal,FisherHe,MouwJaco,,,FairfaxJ,AllenKir,SaulNoah,MouwJaco,FisherHe,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,840
2019-04-05 19:24,AUDL,Dallas Roughnecks,9,D,6,2,Defense,Pull,,,HartzogJ,6.997,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,PolkJake,LavioleA,,,,,,,,,,,,,,,,,,,,,,934
2019-04-05 19:24,AUDL,Dallas Roughnecks,9,D,6,2,Defense,Throwaway,,,Anonymous,,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,PolkJake,LavioleA,,,,,,,,,,,,,,,,,,,,,,938
2019-04-05 19:24,AUDL,Dallas Roughnecks,9,D,6,2,Offense,Goal,YanuckSo,WardRoss,,,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,PolkJake,LavioleA,,,,,,,,,,,,,,,,,,,,,,941
2019-04-05 19:24,AUDL,Dallas Roughnecks,31,D,6,3,Defense,Pull,,,SaulNoah,8.053,HastingJ,SaulNoah,McKelveA,RichardD,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,1004
2019-04-05 19:24,AUDL,Dallas Roughnecks,31,D,6,3,Defense,Goal,,,Anonymous,,HastingJ,SaulNoah,McKelveA,RichardD,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,1033
2019-04-05 19:24,AUDL,Dallas Roughnecks,7,O,7,3,Offense,Goal,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1111
2019-04-05 19:24,AUDL,Dallas Roughnecks,45,D,7,4,Defense,PullOb,,,SaulNoah,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1173
2019-04-05 19:24,AUDL,Dallas Roughnecks,45,D,7,4,Defense,Goal,,,Anonymous,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1216
2019-04-05 19:24,AUDL,Dallas Roughnecks,31,O,7,5,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,MouwJaco,FisherHe,RichardD,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1275
2019-04-05 19:24,AUDL,Dallas Roughnecks,31,O,7,5,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,MouwJaco,FisherHe,RichardD,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1285
2019-04-05 19:24,AUDL,Dallas Roughnecks,31,O,7,5,Offense,Catch,FairfaxJ,MouwJaco,,,FairfaxJ,MouwJaco,FisherHe,RichardD,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1296
2019-04-05 19:24,AUDL,Dallas Roughnecks,31,O,7,5,Offense,Throwaway,MouwJaco,Anonymous,,,FairfaxJ,MouwJaco,FisherHe,RichardD,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1300
2019-04-05 19:24,AUDL,Dallas Roughnecks,31,O,7,5,Defense,Goal,,,Anonymous,,FairfaxJ,MouwJaco,FisherHe,RichardD,LavioleA,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1304
2019-04-05 19:24,AUDL,Dallas Roughnecks,50,O,8,5,Offense,Catch,TaylorEr,SaulNoah,,,FairfaxJ,SaulNoah,FisherHe,WardRoss,PolkJake,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1369
2019-04-05 19:24,AUDL,Dallas Roughnecks,50,O,8,5,Offense,Goal,SaulNoah,FreystaM,,,FairfaxJ,SaulNoah,FisherHe,WardRoss,PolkJake,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1417
2019-04-05 19:24,AUDL,Dallas Roughnecks,7,D,8,5,Cessation,EndOfFirstQuarter,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,1423
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Defense,Pull,,,SaulNoah,5.148,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1598
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Defense,Throwaway,,,Anonymous,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1627
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,YanuckSo,SaulNoah,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1631
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,SaulNoah,YanuckSo,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1635
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,YanuckSo,HartzogJ,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1639
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,HartzogJ,YanuckSo,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1643
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,YanuckSo,WardRoss,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1647
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,WardRoss,RichardD,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1651
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,RichardD,FreystaM,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1655
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,FreystaM,WardRoss,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1659
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,WardRoss,FreystaM,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1663
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,FreystaM,WardRoss,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1667
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,WardRoss,HartzogJ,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1671
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Catch,HartzogJ,SaulNoah,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1675
2019-04-05 19:24,AUDL,Dallas Roughnecks,83,D,9,5,Offense,Goal,SaulNoah,McAllisT,,,SaulNoah,HartzogJ,RichardD,WardRoss,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,1679
2019-04-05 19:24,AUDL,Dallas Roughnecks,53,D,9,6,Defense,Pull,,,YanuckSo,7.474,HastingJ,NordgreJ,YanuckSo,PolkJake,MunizCha,MitchelT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,1728
2019-04-05 19:24,AUDL,Dallas Roughnecks,53,D,9,6,Defense,Goal,,,Anonymous,,HastingJ,NordgreJ,YanuckSo,PolkJake,MunizCha,MitchelT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,1779
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1888
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1895
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,FisherHe,LavioleA,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1899
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,LavioleA,FairfaxJ,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1904
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,FairfaxJ,LavioleA,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1906
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,LavioleA,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1912
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,FisherHe,LavioleA,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1916
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,LavioleA,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1918
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,FisherHe,LavioleA,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1922
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1924
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1930
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1931
2019-04-05 19:24,AUDL,Dallas Roughnecks,48,O,10,6,Offense,Goal,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,1934
2019-04-05 19:24,AUDL,Dallas Roughnecks,49,D,10,7,Defense,PullOb,,,SaulNoah,,HastingJ,SaulNoah,HartzogJ,NordgreJ,WardRoss,YanuckSo,PolkJake,,,,,,,,,,,,,,,,,,,,,,1972
2019-04-05 19:24,AUDL,Dallas Roughnecks,49,D,10,7,Defense,Goal,,,Anonymous,,HastingJ,SaulNoah,HartzogJ,NordgreJ,WardRoss,YanuckSo,PolkJake,,,,,,,,,,,,,,,,,,,,,,2019
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2082
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2083
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2092
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2096
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2100
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,TaylorEr,MunizCha,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2104
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,MunizCha,LavioleA,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2108
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,LavioleA,FairfaxJ,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2112
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,FairfaxJ,LavioleA,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2116
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,LavioleA,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2120
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2124
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2128
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2132
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2136
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,AllenKir,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2140
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,FisherHe,MitchelT,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2144
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,MitchelT,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2148
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2152
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2156
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Catch,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2160
2019-04-05 19:24,AUDL,Dallas Roughnecks,85,O,11,7,Offense,Goal,FisherHe,LavioleA,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2165
2019-04-05 19:24,AUDL,Dallas Roughnecks,108,D,11,8,Defense,Pull,,,McAllisT,6.2,SaulNoah,McKelveA,RichardD,YanuckSo,FreystaM,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,2223
2019-04-05 19:24,AUDL,Dallas Roughnecks,108,D,11,8,Defense,D,,,FreystaM,,SaulNoah,McKelveA,RichardD,YanuckSo,FreystaM,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,2262
2019-04-05 19:24,AUDL,Dallas Roughnecks,108,D,11,8,Offense,Catch,SaulNoah,YanuckSo,,,SaulNoah,McKelveA,RichardD,YanuckSo,FreystaM,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,2267
2019-04-05 19:24,AUDL,Dallas Roughnecks,108,D,11,8,Offense,Catch,YanuckSo,McAllisT,,,SaulNoah,McKelveA,RichardD,YanuckSo,FreystaM,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,2270
2019-04-05 19:24,AUDL,Dallas Roughnecks,108,D,11,8,Offense,Throwaway,McAllisT,Anonymous,,,SaulNoah,McKelveA,RichardD,YanuckSo,FreystaM,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,2275
2019-04-05 19:24,AUDL,Dallas Roughnecks,108,D,11,8,Defense,Goal,,,Anonymous,,SaulNoah,McKelveA,RichardD,YanuckSo,FreystaM,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,2329
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2398
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2407
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,LavioleA,FairfaxJ,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2411
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,FairfaxJ,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2415
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,TaylorEr,MunizCha,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2420
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,MunizCha,MouwJaco,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2424
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,MouwJaco,LavioleA,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2434
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,LavioleA,FairfaxJ,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2450
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,FairfaxJ,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2456
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,TaylorEr,LavioleA,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2460
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2464
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,TaylorEr,MouwJaco,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2468
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,MouwJaco,FisherHe,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2472
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2476
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Catch,TaylorEr,FisherHe,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2480
2019-04-05 19:24,AUDL,Dallas Roughnecks,113,O,12,8,Offense,Goal,FisherHe,AllenKir,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,2509
2019-04-05 19:24,AUDL,Dallas Roughnecks,16,D,12,9,Defense,Pull,,,McAllisT,6.582,HastingJ,SaulNoah,HartzogJ,NordgreJ,WardRoss,PolkJake,McAllisT,,,,,,,,,,,,,,,,,,,,,,2557
2019-04-05 19:24,AUDL,Dallas Roughnecks,16,D,12,9,Defense,Goal,,,Anonymous,,HastingJ,SaulNoah,HartzogJ,NordgreJ,WardRoss,PolkJake,McAllisT,,,,,,,,,,,,,,,,,,,,,,2571
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,AllenKir,TaylorEr,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2628
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,TaylorEr,McKelveA,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2641
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,McKelveA,AllenKir,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2646
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,AllenKir,MitchelT,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2650
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,MitchelT,FisherHe,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2653
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,FisherHe,AllenKir,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2656
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,AllenKir,FairfaxJ,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2659
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,FairfaxJ,McKelveA,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2661
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Throwaway,McKelveA,Anonymous,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2668
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Defense,D,,,McAllisT,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2830
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Catch,TaylorEr,FairfaxJ,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2942
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Offense,Throwaway,FairfaxJ,Anonymous,,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,2947
2019-04-05 19:24,AUDL,Dallas Roughnecks,438,O,12,10,Defense,Goal,,,Anonymous,,HastingJ,FairfaxJ,MouwJaco,FisherHe,NordgreJ,WardRoss,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,McKelveA,FreystaM,,,,,,,,,,,,,,3064
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,SaulNoah,TaylorEr,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3126
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3134
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,FairfaxJ,MitchelT,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3138
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,MitchelT,TaylorEr,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3148
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,TaylorEr,SaulNoah,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3151
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,SaulNoah,MunizCha,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3155
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,MunizCha,SaulNoah,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3159
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Catch,SaulNoah,MouwJaco,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3161
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Offense,Throwaway,MouwJaco,Anonymous,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3163
2019-04-05 19:24,AUDL,Dallas Roughnecks,43,O,12,10,Cessation,Halftime,,,,,FairfaxJ,SaulNoah,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,3167
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,TaylorEr,AllenKir,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4006
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,AllenKir,TaylorEr,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4015
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,TaylorEr,FairfaxJ,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4019
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,FairfaxJ,TaylorEr,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4022
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,TaylorEr,MunizCha,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4026
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Throwaway,MunizCha,Anonymous,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4030
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Defense,D,,,TaylorEr,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4046
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,LavioleA,TaylorEr,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4066
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,TaylorEr,FisherHe,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4081
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,FisherHe,MunizCha,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4084
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,MunizCha,FisherHe,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4088
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,FisherHe,TaylorEr,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4092
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Throwaway,TaylorEr,Anonymous,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4096
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Defense,Throwaway,,,Anonymous,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4130
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Throwaway,TaylorEr,Anonymous,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4159
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Defense,Throwaway,,,Anonymous,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4173
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,AllenKir,LavioleA,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4176
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,LavioleA,AllenKir,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4180
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,AllenKir,MunizCha,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4184
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Catch,MunizCha,MitchelT,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4188
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Offense,Throwaway,MitchelT,Anonymous,,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4192
2019-04-05 19:24,AUDL,Dallas Roughnecks,355,O,12,11,Defense,Goal,,,Anonymous,,HastingJ,FairfaxJ,FisherHe,WardRoss,YanuckSo,McAllisT,LavioleA,MunizCha,MitchelT,TaylorEr,SaulNoah,AllenKir,FreystaM,LynchJoh,,,,,,,,,,,,,,,4359
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4417
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4425
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,FairfaxJ,AllenKir,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4429
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,AllenKir,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4436
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Throwaway,FisherHe,Anonymous,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4441
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Defense,Throwaway,,,Anonymous,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4449
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,LavioleA,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4460
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,FisherHe,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4464
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,TaylorEr,MouwJaco,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4470
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,MouwJaco,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4473
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4477
2019-04-05 19:24,AUDL,Dallas Roughnecks,66,O,13,11,Offense,Goal,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,McKelveA,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4481
2019-04-05 19:24,AUDL,Dallas Roughnecks,53,D,13,12,Defense,Pull,,,SaulNoah,4.733,HastingJ,SaulNoah,RichardD,NordgreJ,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,4534
2019-04-05 19:24,AUDL,Dallas Roughnecks,53,D,13,12,Defense,Goal,,,Anonymous,,HastingJ,SaulNoah,RichardD,NordgreJ,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,4585
2019-04-05 19:24,AUDL,Dallas Roughnecks,28,O,14,12,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4644
2019-04-05 19:24,AUDL,Dallas Roughnecks,28,O,14,12,Offense,Catch,TaylorEr,MitchelT,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4652
2019-04-05 19:24,AUDL,Dallas Roughnecks,28,O,14,12,Offense,Catch,MitchelT,FairfaxJ,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4666
2019-04-05 19:24,AUDL,Dallas Roughnecks,28,O,14,12,Offense,Goal,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,MouwJaco,FisherHe,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4670
2019-04-05 19:24,AUDL,Dallas Roughnecks,41,D,14,13,Defense,Pull,,,HartzogJ,6.665,HartzogJ,McKelveA,WardRoss,YanuckSo,PolkJake,LavioleA,LynchJoh,,,,,,,,,,,,,,,,,,,,,,4724
2019-04-05 19:24,AUDL,Dallas Roughnecks,41,D,14,13,Defense,Goal,,,Anonymous,,HartzogJ,McKelveA,WardRoss,YanuckSo,PolkJake,LavioleA,LynchJoh,,,,,,,,,,,,,,,,,,,,,,4763
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,SaulNoah,AllenKir,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4833
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,AllenKir,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4841
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Throwaway,TaylorEr,Anonymous,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4850
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Defense,Throwaway,,,Anonymous,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4871
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,SaulNoah,AllenKir,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4886
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,AllenKir,SaulNoah,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4889
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,SaulNoah,FairfaxJ,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4896
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,FairfaxJ,MitchelT,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4900
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,MitchelT,FreystaM,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4904
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,FreystaM,AllenKir,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4908
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,AllenKir,FisherHe,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4912
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,FisherHe,SaulNoah,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4916
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,SaulNoah,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4920
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,TaylorEr,SaulNoah,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4924
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,SaulNoah,TaylorEr,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4928
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4930
2019-04-05 19:24,AUDL,Dallas Roughnecks,101,O,15,13,Offense,Goal,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,SaulNoah,FisherHe,FreystaM,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,4932
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Defense,Pull,,,NordgreJ,5.411,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,4987
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Defense,D,,,RichardD,,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,5015
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Offense,Catch,RichardD,WardRoss,,,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,5021
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Offense,Catch,WardRoss,YanuckSo,,,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,5025
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Offense,Throwaway,YanuckSo,Anonymous,,,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,5029
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Defense,D,,,YanuckSo,,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,5062
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Offense,Throwaway,YanuckSo,Anonymous,,,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,5077
2019-04-05 19:24,AUDL,Dallas Roughnecks,107,D,15,14,Defense,Goal,,,Anonymous,,HastingJ,HartzogJ,RichardD,NordgreJ,WardRoss,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,5092
2019-04-05 19:24,AUDL,Dallas Roughnecks,17,O,15,15,Offense,Throwaway,SaulNoah,Anonymous,,,FairfaxJ,AllenKir,SaulNoah,MouwJaco,FisherHe,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5215
2019-04-05 19:24,AUDL,Dallas Roughnecks,17,O,15,15,Defense,Goal,,,Anonymous,,FairfaxJ,AllenKir,SaulNoah,MouwJaco,FisherHe,LavioleA,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5230
2019-04-05 19:24,AUDL,Dallas Roughnecks,198,O,15,15,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,SaulNoah,FisherHe,RichardD,PolkJake,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5341
2019-04-05 19:24,AUDL,Dallas Roughnecks,198,O,15,15,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,SaulNoah,FisherHe,RichardD,PolkJake,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5349
2019-04-05 19:24,AUDL,Dallas Roughnecks,198,O,15,15,Offense,Throwaway,FreystaM,Anonymous,,,FairfaxJ,SaulNoah,FisherHe,RichardD,PolkJake,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5357
2019-04-05 19:24,AUDL,Dallas Roughnecks,198,O,15,15,Defense,Throwaway,,,Anonymous,,FairfaxJ,SaulNoah,FisherHe,RichardD,PolkJake,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5380
2019-04-05 19:24,AUDL,Dallas Roughnecks,198,O,15,15,Cessation,EndOfThirdQuarter,,,,,FairfaxJ,SaulNoah,FisherHe,RichardD,PolkJake,FreystaM,TaylorEr,,,,,,,,,,,,,,,,,,,,,,5537
2019-04-05 19:24,AUDL,Dallas Roughnecks,72,D,15,16,Defense,Pull,,,SaulNoah,4.681,HastingJ,SaulNoah,HartzogJ,RichardD,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,5693
2019-04-05 19:24,AUDL,Dallas Roughnecks,72,D,15,16,Defense,Goal,,,Anonymous,,HastingJ,SaulNoah,HartzogJ,RichardD,YanuckSo,FreystaM,McAllisT,,,,,,,,,,,,,,,,,,,,,,5763
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,AllenKir,TaylorEr,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5817
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,TaylorEr,MunizCha,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5831
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,MunizCha,MitchelT,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5835
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,MitchelT,McKelveA,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5839
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,McKelveA,TaylorEr,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5844
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,TaylorEr,McKelveA,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5851
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,McKelveA,TaylorEr,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5856
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,TaylorEr,McKelveA,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5860
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,McKelveA,FisherHe,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5864
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Throwaway,FisherHe,Anonymous,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,5869
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Defense,Throwaway,,,Anonymous,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6014
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,TaylorEr,FisherHe,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6032
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Throwaway,TaylorEr,Anonymous,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6128
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Defense,Throwaway,,,Anonymous,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6273
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,YanuckSo,HastingJ,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6293
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,HastingJ,YanuckSo,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6298
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,YanuckSo,HastingJ,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6302
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,HastingJ,WardRoss,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6308
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,WardRoss,YanuckSo,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6316
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,YanuckSo,LynchJoh,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6324
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Catch,LynchJoh,YanuckSo,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6328
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Offense,Throwaway,YanuckSo,Anonymous,,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6331
2019-04-05 19:24,AUDL,Dallas Roughnecks,613,O,15,17,Defense,Goal,,,Anonymous,,HastingJ,RichardD,WardRoss,YanuckSo,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6428
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,LavioleA,TaylorEr,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6495
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,TaylorEr,FreystaM,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6504
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,FreystaM,MouwJaco,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6508
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,MouwJaco,FreystaM,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6512
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,FreystaM,MouwJaco,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6512
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,MouwJaco,FisherHe,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6516
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,FisherHe,MouwJaco,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6520
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,MouwJaco,FisherHe,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6524
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Catch,FisherHe,LavioleA,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6528
2019-04-05 19:24,AUDL,Dallas Roughnecks,39,O,16,17,Offense,Goal,LavioleA,FreystaM,,,FairfaxJ,MouwJaco,FisherHe,FreystaM,LavioleA,MunizCha,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6532
2019-04-05 19:24,AUDL,Dallas Roughnecks,45,D,16,18,Defense,Pull,,,SaulNoah,6.422,HastingJ,SaulNoah,HartzogJ,RichardD,NordgreJ,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,6581
2019-04-05 19:24,AUDL,Dallas Roughnecks,45,D,16,18,Defense,Goal,,,Anonymous,,HastingJ,SaulNoah,HartzogJ,RichardD,NordgreJ,YanuckSo,McAllisT,,,,,,,,,,,,,,,,,,,,,,6624
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Catch,MunizCha,AllenKir,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6680
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Catch,AllenKir,MunizCha,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6689
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Catch,MunizCha,FairfaxJ,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6693
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Catch,FairfaxJ,LavioleA,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6697
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Catch,LavioleA,MunizCha,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6703
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Catch,MunizCha,TaylorEr,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6707
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Catch,TaylorEr,FairfaxJ,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6712
2019-04-05 19:24,AUDL,Dallas Roughnecks,42,O,17,18,Offense,Goal,FairfaxJ,FisherHe,,,FairfaxJ,AllenKir,FisherHe,LavioleA,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6720
2019-04-05 19:24,AUDL,Dallas Roughnecks,143,D,17,19,Defense,Pull,,,SaulNoah,5.965,SaulNoah,RichardD,NordgreJ,WardRoss,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6777
2019-04-05 19:24,AUDL,Dallas Roughnecks,143,D,17,19,Defense,Goal,,,Anonymous,,SaulNoah,RichardD,NordgreJ,WardRoss,PolkJake,McAllisT,LynchJoh,,,,,,,,,,,,,,,,,,,,,,6918
2019-04-05 19:24,AUDL,Dallas Roughnecks,121,O,17,19,Offense,Catch,TaylorEr,AllenKir,,,FairfaxJ,AllenKir,FisherHe,FreystaM,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6983
2019-04-05 19:24,AUDL,Dallas Roughnecks,121,O,17,19,Offense,Catch,AllenKir,MunizCha,,,FairfaxJ,AllenKir,FisherHe,FreystaM,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6988
2019-04-05 19:24,AUDL,Dallas Roughnecks,121,O,17,19,Offense,Throwaway,MunizCha,Anonymous,,,FairfaxJ,AllenKir,FisherHe,FreystaM,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,6995
2019-04-05 19:24,AUDL,Dallas Roughnecks,121,O,17,19,Cessation,GameOver,,,,,FairfaxJ,AllenKir,FisherHe,FreystaM,MunizCha,MitchelT,TaylorEr,,,,,,,,,,,,,,,,,,,,,,7102
'''