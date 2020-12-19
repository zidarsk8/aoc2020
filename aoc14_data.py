test_data = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip()


test_data2 = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[9] = 11
mem[10] = 102
mem[9] = 0
""".strip()

test_data3 = """
mask = X10X11X1000101X1XX001100001X101X0111
mem[27041] = 56559
mem[43069] = 56082467
mem[55125] = 25536
mem[13313] = 3968
mask = 0X01110110X10101X01100110000X0X010X0
mem[51810] = 586700041
mem[5546] = 73582083
mem[64563] = 1709385
mask = X10X1X01000X1XXX1011010X0101001X1100
mem[55081] = 164951
mem[57902] = 941479
mem[64412] = 168227
mem[38991] = 7285
mem[32442] = 4026389
mem[13462] = 11389
""".strip()


test_data4 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip()


data = """
mask = X10X11X1000101X1XX001100001X101X0111
mem[27041] = 56559
mem[43069] = 56082467
mem[55125] = 25536
mem[13313] = 3968
mask = 0X01110110X10101X01100110000X0X010X0
mem[51810] = 586700041
mem[5546] = 73582083
mem[64563] = 1709385
mask = X10X1X01000X1XXX1011010X0101001X1100
mem[55081] = 164951
mem[57902] = 941479
mem[64412] = 168227
mem[38991] = 7285
mem[32442] = 4026389
mem[13462] = 11389
mask = 100XX0010X000001X1X1000110011X000011
mem[30898] = 16273
mem[58759] = 129155
mem[32283] = 16275
mem[40822] = 5428787
mask = 1101110X1101011XX10100111101XX1X0011
mem[49575] = 64412
mem[27128] = 4116
mem[44802] = 1524861
mem[64022] = 21246
mem[43630] = 40764
mask = 1X0X110111010XX111010111X101X0011011
mem[48341] = 23417
mem[53479] = 235442
mem[18336] = 94965893
mem[57351] = 162640
mem[57629] = 1482328
mem[26659] = 30905751
mask = XX0010001X0000011111X1X111X10X11X0X1
mem[24841] = 117268
mem[40922] = 620521271
mem[15784] = 9554135
mem[34841] = 73813
mem[26214] = 1046646796
mem[51219] = 342
mask = 01011X010001X11111010110X1000000011X
mem[30384] = 10767
mem[30180] = 3038
mem[41792] = 1794799
mem[22454] = 141484
mem[8961] = 138657
mask = 1X01010100001X11100100X000X00000X1X0
mem[62834] = 21881
mem[32225] = 113149539
mem[50218] = 84165
mem[39558] = 216497715
mask = 01X0010XX00011X1X0011X001000XX110011
mem[58102] = 854
mem[30215] = 3351
mem[33733] = 166
mem[5725] = 12102
mem[40925] = 663163
mem[4700] = 11609
mem[46222] = 247699901
mask = XX110X11010101101101001XXX1X1X100011
mem[25668] = 1311480
mem[15110] = 43047
mem[20494] = 621
mem[42552] = 885
mem[676] = 440298427
mem[47591] = 1439872
mem[44891] = 239995
mask = 11011XXX0100X001X10X10010110010X11X1
mem[7814] = 84184
mem[54268] = 2433599
mem[50873] = 11428
mem[20156] = 42428
mem[4576] = 13692368
mask = 11010X01100001X110X1X10001X101101X10
mem[40524] = 798
mem[47191] = 3260486
mem[18798] = 86012101
mem[41247] = 21300057
mem[54268] = 74197872
mem[53415] = 68475
mask = 010X1100100X1100X1010011X0X0X0011101
mem[15154] = 7956
mem[43012] = 897
mem[58152] = 25845
mem[766] = 172082371
mem[52128] = 31341204
mask = 1X00X00X110000X111X110XX0111001X0X11
mem[23567] = 917031
mem[35639] = 1135
mem[46408] = 26253
mem[51984] = 269805971
mem[18161] = 145505
mask = 010X100101010X1110X10XX00X11001X0110
mem[39575] = 59052182
mem[44818] = 1753773
mem[54049] = 9062079
mem[7021] = 23033
mask = 1101110111000X0111000010X1010100XX00
mem[1943] = 61503738
mem[61496] = 4688484
mem[12496] = 3724
mem[43497] = 64222
mem[53687] = 7996
mask = 11XXX0010X00001X10XX0000010X0111011X
mem[435] = 14192652
mem[3765] = 846967
mem[61166] = 13875665
mask = 0100010110001X111XXXX100000001010111
mem[3750] = 1921
mem[40035] = 7716582
mem[59566] = 993057
mem[57732] = 1389
mask = 0100000110X00110X100011001XX1X011010
mem[40412] = 246706
mem[63492] = 18123
mem[25668] = 53187
mem[21553] = 25476
mem[30692] = 36784
mem[3183] = 32438
mask = 110X0101X000X11110X11000X010100XX11X
mem[38615] = 506
mem[24603] = 737880
mem[21866] = 390846
mem[4108] = 2001313
mem[44257] = 31442716
mem[41468] = 7966
mem[57394] = 783646
mask = 0X011001100X00111X0110110001X1011101
mem[24387] = 10182
mem[31736] = 115136274
mem[28984] = 2353
mem[2475] = 109336
mask = 110X100X0X00000X1001100X100010000101
mem[51542] = 8298665
mem[57871] = 101098400
mem[50403] = 10935230
mem[22710] = 1959
mem[37641] = 114119
mask = 11X1010X100001X110X110001100X0110011
mem[57394] = 29625020
mem[11168] = 1029
mem[9347] = 1826
mem[11334] = 594
mem[62531] = 2201943
mask = 0X1X01010101X11X1101111X1X00X1010111
mem[41378] = 58920
mem[27145] = 554
mem[60014] = 7131
mask = 11XXX1110X00000X0101100101X0011001X1
mem[28366] = 290247
mem[63097] = 177936
mem[18333] = 14036
mask = 10011X0010X110111011010010X10X001100
mem[52923] = 65816388
mem[23341] = 9880982
mem[15175] = 22538
mask = X101X0110X0100111X10111110100XX10X01
mem[62215] = 13184563
mem[13801] = 49239763
mem[12496] = 892859
mem[37788] = 7710
mem[60433] = 8951271
mask = X11100010X00X010X0000X00000001110110
mem[18584] = 1767
mem[1250] = 44242023
mem[54337] = 1202
mem[16284] = 7015
mask = 11X1X1011000X11X10011010X1X0X00100X1
mem[63358] = 13288368
mem[42217] = 107319
mem[27988] = 123244922
mem[33860] = 182239
mem[40015] = 857415
mem[9829] = 1552
mask = 0101X101100X110X101110X1XX000X0101XX
mem[5707] = 623141
mem[63170] = 3540
mem[49303] = 5946356
mem[34003] = 31894390
mask = 0X010000010001XX1X0101000XXXX000X011
mem[65195] = 9789
mem[49527] = 35294934
mem[61780] = 27702
mem[15175] = 12753075
mem[19444] = 312835
mem[30215] = 26235
mem[56607] = 1184
mask = X101110X1001X00X1011XX01111X00000100
mem[11529] = 202692
mem[7212] = 12087618
mem[13649] = 4152
mem[54165] = 36475777
mem[3587] = 59730191
mask = X10111011101X0X11101111110X100100101
mem[32820] = 988109
mem[58886] = 774558
mem[19222] = 37482
mask = 11010XX1X000011X10110000100001011010
mem[56490] = 41313
mem[60014] = 24800
mem[60019] = 3393
mask = X1000101100011X1X001X1101000000101X1
mem[59526] = 266367133
mem[4762] = 740776
mem[2900] = 137498
mem[19079] = 61895
mem[33262] = 4863
mask = X1011X0XX0X0X11010011X00100011X01X10
mem[48337] = 1047
mem[7814] = 11885727
mem[30993] = 170945
mem[39628] = 1313283
mask = 110X01011000011X100X1101X100X00X0001
mem[46408] = 156741
mem[52622] = 3088962
mem[15423] = 518000
mem[64701] = 514808438
mask = 110101X110000X1X10X11010X110011X1111
mem[43254] = 387
mem[58713] = 8724789
mem[26335] = 544255113
mem[11424] = 47914958
mem[36656] = 224193
mask = 010000XXX0X0011110X10110000X01001X01
mem[63579] = 52105299
mem[37046] = 1134
mask = 11111X0110001X10X001X111X10100111111
mem[61324] = 31303686
mem[64060] = 1610
mem[39793] = 1958162
mem[46164] = 668042
mem[16116] = 13803
mem[35215] = 448312344
mask = X10101X1100011111001101001X0110001X1
mem[7844] = 760372
mem[44693] = 16675
mem[11334] = 16652
mask = 011101X1010101111XX110010101X01X0011
mem[47181] = 37171
mem[57629] = 49275889
mem[18322] = 500908019
mem[46549] = 834444470
mem[13951] = 574868
mem[26538] = 787853
mask = XX011X011100X00111X1X0X001X011X11010
mem[64949] = 162355279
mem[57407] = 3350
mem[43929] = 203041
mask = 1101101100X100110X010001101000110XX1
mem[32532] = 32712949
mem[51621] = 1546586
mem[22570] = 251922029
mem[10937] = 3154069
mem[25790] = 49139
mask = 01011101XX0111X110111011XXX01001010X
mem[24482] = 117679
mem[60433] = 714
mem[23257] = 69062735
mem[28676] = 15016259
mem[32334] = 4194426
mask = 0X000101100001101001XX101111010101X1
mem[31956] = 796
mem[28984] = 1446991
mem[39810] = 27358954
mem[9234] = 19734706
mem[45123] = 247705194
mem[34003] = 35251
mem[16180] = 804679
mask = 1101XXX00000011010X0111010X010010000
mem[13595] = 284
mem[39575] = 14805
mem[41940] = 27710
mem[48667] = 118527
mem[43689] = 5996
mem[55758] = 3036117
mask = 11011XX10101010111011110000100010X0X
mem[10468] = 8121
mem[45166] = 970006437
mask = 11011001X10000X11XX1XXX00XX011000011
mem[18583] = 2551
mem[32334] = 2009
mem[27128] = 56668016
mem[52052] = 750760
mem[49527] = 46604
mem[49214] = 1061
mem[1791] = 11556
mask = 1X0X0101X000011X1X0100110X001001X011
mem[12346] = 178717508
mem[52270] = 311954237
mem[49864] = 7470000
mask = X101010110000X1X10011X01XX101XX11010
mem[37530] = 80
mem[32958] = 28577227
mem[40585] = 8221
mem[57579] = 1646
mem[50218] = 7908
mask = 010011011X0101X100X10001001X00000111
mem[50694] = 457
mem[13360] = 62444656
mem[4404] = 1266571
mask = X101110X00X110X11X1110X1X011101001XX
mem[23104] = 253935942
mem[14852] = 2270
mem[34981] = 1108
mem[53840] = 146384561
mem[47509] = 60247
mem[23085] = 51902845
mem[58655] = 9691
mask = 1X0XXX1100X1X0110X01111X1110000001X1
mem[60433] = 128268
mem[57082] = 816691399
mem[45011] = 80982
mem[39218] = 1071426371
mask = 11010X011000XX101001X01100001101010X
mem[35350] = 8809868
mem[9433] = 65247
mem[38801] = 2086
mask = 11011101X10XX00X110XX00001X0X110X101
mem[54049] = 8667
mem[46876] = 435193
mem[43949] = 15176016
mem[44664] = 26159
mem[23255] = 895
mask = 01X1X1X1010101111101001111X1X101X1X1
mem[61166] = 504606
mem[61956] = 20721
mem[39929] = 1403
mask = X10X010110000X1110011010110X11110001
mem[40015] = 700480
mem[36436] = 4893
mem[32266] = 25534
mem[41902] = 2988
mem[39810] = 28
mem[41370] = 57925
mem[12356] = 297319
mask = X101111101010XX111X1X01X1X0101X1010X
mem[37641] = 9726
mem[59076] = 168552
mem[45749] = 1746884
mem[17712] = 69612
mem[49214] = 867128713
mem[61637] = 40856300
mem[33365] = 1428019
mask = 1101110X1000X1111X0110001X0001010100
mem[13072] = 10041
mem[53702] = 773477
mem[44645] = 2404420
mem[45439] = 5964
mem[58658] = 208590
mem[44798] = 19402244
mask = 110X11X1100X0111100110001X00X10000X1
mem[10421] = 171265821
mem[12356] = 680301
mem[22675] = 21609725
mask = 011X0111X101011X1X010XX100X010X001X1
mem[32543] = 354353
mem[46511] = 2359
mem[19545] = 27624
mem[27128] = 48860350
mem[4352] = 97594900
mem[7423] = 256
mask = 100XX001010000X11X111X0010X00XX10X10
mem[9234] = 14199
mem[20857] = 105139600
mem[8485] = 397519358
mem[56314] = 191575
mem[56707] = 14956
mem[53089] = 289600
mem[21001] = 13079705
mask = 010111011001XX01X0111001X0XX1001XX0X
mem[106] = 21541596
mem[12371] = 3644659
mem[50177] = 205339532
mem[1812] = 473555543
mem[22675] = 1216737
mask = 1X011001010000X1101100001X1X01X101XX
mem[27858] = 4008
mem[51566] = 49154
mem[4762] = 16827
mem[53603] = 472698
mem[23186] = 5880
mem[53599] = 989
mask = X10X0101100000111001X1XX0X00X1000110
mem[49118] = 921
mem[34859] = 802
mem[55335] = 213213436
mem[12356] = 90675624
mem[34362] = 1372
mem[30455] = 1338
mask = 010100110000001XX001X101011101X1X100
mem[12601] = 13719557
mem[6055] = 1675
mem[22570] = 918
mem[52622] = 2656587
mem[45642] = 5143
mem[16015] = 11484862
mask = 1101X0010100X011X1X100X0X100XX11X111
mem[19222] = 424
mem[59273] = 29846629
mem[17113] = 7689
mem[48356] = 4606
mask = 010X1101X00101010011X00100XXXX1X0X10
mem[15158] = 3693
mem[4535] = 32872078
mem[42138] = 9199883
mem[61166] = 328197677
mem[25980] = 210
mem[38567] = 238946499
mask = X10XX0000X00011X100X1011000111X1X11X
mem[56158] = 7060
mem[1355] = 4692
mem[15605] = 13671929
mem[22570] = 1896780
mem[25653] = 62047211
mem[49303] = 143257122
mask = 1XX11100X01110111011X0X11X11X01000X0
mem[47139] = 5173
mem[33745] = 500428082
mem[55823] = 311
mem[1250] = 296582
mem[63703] = 949
mask = X1011101000X1X0110110X1X0X0110X00110
mem[51810] = 18035546
mem[53428] = 3886
mem[64949] = 645
mem[52996] = 41172825
mem[49452] = 1367
mask = 110XXX011X000X011111110XX010X10X0011
mem[17565] = 16592
mem[49575] = 3981067
mem[4250] = 300364
mem[35350] = 8178
mem[22007] = 21898575
mask = 010X01X110000X101011X001011X111X1X10
mem[18950] = 13300
mem[4487] = 612
mem[12388] = 412719717
mem[44693] = 3118
mask = 1101X10110X0011010010X0100101010X000
mem[48867] = 17605927
mem[8397] = 1860772
mem[39018] = 550228
mem[38250] = 47809475
mem[2450] = 116013203
mem[49776] = 393349
mask = 1101X10110000X11100111X101101100X010
mem[53450] = 656535467
mem[6408] = 21122
mem[40154] = 1342486
mask = 1101100X010X101X0111000101000X101111
mem[4324] = 686588689
mem[64022] = 1565401
mem[35893] = 9127
mem[63924] = 5346
mask = X1011X01XX0X0X111X0111101111X00X0111
mem[18336] = 33319783
mem[9347] = 7493509
mem[6227] = 1816
mem[31665] = 5514016
mem[51408] = 4879
mem[53450] = 114937
mask = 010100XX000000XX10011X0X0011XX011000
mem[46925] = 103
mem[57394] = 965124
mem[15985] = 980924
mem[52270] = 110464
mem[15394] = 1276
mask = XX000100X0X01101X10100XX0XX000001011
mem[13230] = 1399497
mem[64578] = 3309
mem[25149] = 7933
mask = 01010101100X101110X1X00XX00X1111X0X1
mem[16284] = 27584023
mem[46579] = 360009595
mem[30484] = 677717
mem[11059] = 52513896
mem[38700] = 683
mask = 110110X1000X0X11X1XXX11X1000000X0111
mem[16164] = 177
mem[8961] = 6185342
mem[53026] = 72900939
mask = 1XX11X0111001XX11111010X010011111X00
mem[59825] = 37712
mem[42879] = 746543
mem[16391] = 54454690
mem[43036] = 346868
mem[25030] = 38931
mem[5215] = 890634260
mask = 1101110X00001001101111X0XX11001XX100
mem[19490] = 5726
mem[17000] = 16738
mem[61693] = 7616
mem[2295] = 1627
mem[44236] = 269
mem[4389] = 1030099
mem[11170] = 4961
mask = 010X1101101X01011X1110X1X10010X0001X
mem[27835] = 16102
mem[12301] = 8157
mem[38801] = 32685079
mask = X1011101000100111X01011X101110X00111
mem[64949] = 21205
mem[56917] = 416029376
mem[50979] = 2487904
mem[64022] = 2045
mem[13313] = 804618
mem[55628] = 17126
mask = X1010101100X110110X1111X0X00XX0X010X
mem[39628] = 924
mem[39127] = 3978399
mem[36741] = 1917293
mem[62950] = 6997
mask = 01110101010101111X01101XX111X1X0010X
mem[20491] = 500
mem[36269] = 22639420
mem[44179] = 725
mem[48503] = 520056
mem[7514] = 28103
mem[54438] = 410686
mask = 0101XX0X10001X01X01110101100000111X1
mem[45749] = 494350
mem[44246] = 3578
mem[15900] = 1654
mem[32209] = 218393668
mem[30484] = 213583441
mem[25092] = 55738
mask = 01000X011000011X1X0X010100XXXX011110
mem[39783] = 25297
mem[60998] = 35841298
mem[54570] = 2329
mem[41435] = 43307534
mem[55264] = 375757
mem[63681] = 112957
mask = 1101010XX000X1101001101000XX00X1X001
mem[55707] = 16304353
mem[14995] = 11351
mem[12346] = 746754510
mem[11376] = 339
mem[2762] = 51886
mem[26983] = 4316816
mask = 0100X101100001XX1011100101X010111100
mem[25172] = 183861621
mem[5742] = 14878506
mask = X10X01011000X1X010X110X0XX1X01010110
mem[51566] = 2828
mem[18567] = 265
mem[16314] = 423578
mem[5215] = 239
mem[42065] = 2230191
mask = 010X1X010X0X0111X00X1110X001XX010111
mem[10367] = 9431
mem[23257] = 10057
mem[37558] = 789
mem[2683] = 83395426
mem[19984] = 148832616
mask = 110X0101110X0X0111111000001001XX10XX
mem[47509] = 998
mem[41953] = 20146419
mem[44664] = 302148902
mem[63696] = 1160792
mem[17933] = 98120645
mem[49199] = 931033
mem[7279] = 20085
mask = 11X10101X0XX111X101110100X10XX001010
mem[34951] = 7290
mem[40015] = 39139
mem[36460] = 53336927
mask = 0100X10X1000110X1X01X1110X1X0X1100X1
mem[45422] = 1972
mem[54204] = 3976851
mem[53302] = 100688
mem[39162] = 179175
mem[46756] = 354581686
mem[30570] = 4338666
mask = XX01X0X1000X0X11X001011001100XX10101
mem[57138] = 9547723
mem[32548] = 17740188
mem[62284] = 300055571
mask = 010X01011000XXXX1001101X00X01001XX01
mem[21470] = 78562
mem[44450] = 77626
mem[19490] = 33608425
mem[4762] = 21717
mem[26613] = 40
""".strip()
