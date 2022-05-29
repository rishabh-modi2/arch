# import os, subprocess
do = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 13300, 13400, 13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100, 15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900, 16000, 16100, 16200, 16300, 16400, 16500, 16600, 16700, 16800, 16900, 17000, 17100, 17200, 17300, 17400, 17500, 17600, 17700, 17800, 17900, 18000, 18100, 18200, 18300, 18400, 18500, 18600, 18700, 18800, 18900, 19000, 19100, 19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000, 20100, 20200, 20300, 20400, 20500, 20600, 20700, 20800, 20900, 21000, 21100, 21200, 21300, 21400, 21500, 21600, 21700, 21800, 21900, 22000, 22100, 22200, 22300, 22400, 22500, 22600, 22700, 22800, 22900, 23000, 23100, 23200, 23300, 23400, 23500, 23600, 23700, 23800, 23900, 24000, 24100, 24200, 24300, 24400, 24500, 24600, 24700, 24800, 24900, 25000, 25100, 25200, 25300, 25400, 25500, 25600, 25700, 25800, 25900, 26000, 26100, 26200, 26300, 26400, 26500, 26600, 26700, 26800, 26900, 27000, 27100, 27200, 27300, 27400, 27500, 27600, 27700, 27800, 27900, 28000, 28100, 28200, 28300, 28400, 28500, 28600, 28700, 28800, 28900, 29000, 29100, 29200, 29300, 29400, 29500, 29600, 29700, 29800, 29900, 30000, 30100, 30200, 30300, 30400, 30500, 30600, 30700, 30800, 30900, 31000, 31100, 31200, 31300, 31400, 31500, 31600, 31700, 31800, 31900, 32000, 32100, 32200, 32300, 32400, 32500, 32600, 32700, 32800, 32900, 33000, 33100, 33200, 33300, 33400, 33500, 33600, 33700, 33800, 33900, 34000, 34100, 34200, 34300, 34400, 34500, 34600, 34700, 34800, 34900, 35000, 35100, 35200, 35300, 35400, 35500, 35600, 35700, 35800, 35900, 36000, 36100, 36200, 36300, 36400, 36500, 36600, 36700, 36800, 36900, 37000, 37100, 37200, 37300, 37400, 37500, 37600, 37700, 37800, 37900, 38000, 38100, 38200, 38300, 38400, 38500, 38600, 38700, 38800, 38900, 39000, 39100, 39200, 39300, 39400, 39500, 39600, 39700, 39800, 39900, 40000, 40100, 40200, 40300, 40400, 40500, 40600, 40700, 40800, 40900, 41000, 41100, 41200, 41300, 41400, 41500, 41600, 41700, 41800, 41900, 42000, 42100, 42200, 42300, 42400, 42500, 42600, 42700, 42800, 42900, 43000, 43100, 43200, 43300, 43400, 43500, 43600, 43700, 43800, 43900, 44000, 44100, 44200, 44300, 44400, 44500, 44600, 44700, 44800, 44900, 45000, 45100, 45200, 45300, 45400, 45500, 45600, 45700, 45800, 45900, 46000, 46100, 46200, 46300, 46400, 46500, 46600, 46700, 46800, 46900, 47000, 47100, 47200, 47300, 47400, 47500, 47600, 47700, 47800, 47900, 48000, 48100, 48200, 48300, 48400, 48500, 48600, 48700, 48800, 48900, 49000, 49100, 49200, 49300, 49400, 49500, 49600, 49700, 49800, 49900, 50000, 50100, 50200, 50300, 50400, 50500, 50600, 50700, 50800, 50900, 51000, 51100, 51200, 51300, 51400, 51500, 51600, 51700, 51800, 51900, 52000, 52100, 52200, 52300, 52400, 52500, 52600, 52700, 52800, 52900, 53000, 53100, 53200, 53300, 53400, 53500, 53600, 53700, 53800, 53900, 54000, 54100, 54200, 54300, 54400, 54500, 54600, 54700, 54800, 54900, 55000, 55100, 55200, 55300, 55400, 55500, 55600, 55700, 55800, 55900, 56000, 56100, 56200, 56300, 56400, 56500, 56600, 56700, 56800, 56900, 57000, 57100, 57200, 57300, 57400, 57500, 57600, 57700, 57800, 57900, 58000, 58100, 58200, 58300, 58400, 58500, 58600, 58700, 58800, 58900, 59000, 59100, 59200, 59300, 59400, 59500, 59600, 59700, 59800, 59900, 60000, 60100, 60200, 60300, 60400, 60500, 60600, 60700, 60800, 60900, 61000, 61100, 61200, 61300, 61400, 61500, 61600, 61700, 61800, 61900, 62000, 62100, 62200, 62300, 62400, 62500, 62600, 62700, 62800, 62900, 63000, 63100, 63200, 63300, 63400, 63500, 63600, 63700, 63800, 63900, 64000, 64100, 64200, 64300, 64400, 64500, 64600, 64700, 64800, 64900, 65000, 65100, 65200, 65300, 65400, 65500, 65600, 65700, 65800, 65900, 66000, 66100, 66200, 66300, 66400, 66500, 66600, 66700, 66800, 66900, 67000, 67100, 67200, 67300, 67400, 67500, 67600, 67700, 67800, 67900, 68000, 68100, 68200, 68300, 68400, 68500, 68600, 68700, 68800, 68900, 69000, 69100, 69200, 69300, 69400, 69500, 69600, 69700, 69800, 69900, 70000, 70100, 70200, 70300, 70400, 70500, 70600, 70700, 70800, 70900, 71000, 71100, 71200, 71300, 71400, 71500, 71600, 71700, 71800, 71900, 72000, 72100, 72200, 72300, 72400, 72500, 72600, 72700, 72800, 72900, 73000, 73100, 73200, 73300, 73400, 73500, 73600, 73700, 73800, 73900, 74000, 74100, 74200, 74300, 74400, 74500, 74600, 74700, 74800, 74900, 75000, 75100, 75200, 75300, 75400, 75500, 75600, 75700, 75800, 75900, 76000, 76100, 76200, 76300, 76400, 76500, 76600, 76700, 76800, 76900, 77000, 77100, 77200, 77300, 77400, 77500, 77600, 77700, 77800, 77900, 78000, 78100, 78200, 78300, 78400, 78500, 78600, 78700, 78800, 78900, 79000, 79100, 79200, 79300, 79400, 79500, 79600, 79700, 79800, 79900, 80000, 80100, 80200, 80300, 80400, 80500, 80600, 80700, 80800, 80900, 81000, 81100, 81200, 81300, 81400, 81500, 81600, 81700, 81800, 81900, 82000, 82100, 82200, 82300, 82400, 82500, 82600, 82700, 82800, 82900, 83000, 83100, 83200, 83300, 83400, 83500, 83600, 83700, 83800, 83900, 84000, 84100, 84200, 84300, 84400, 84500, 84600, 84700, 84800, 84900, 85000, 85100, 85200, 85300, 85400, 85500, 85600, 85700, 85800, 85900, 86000, 86100, 86200, 86300, 86400, 86500, 86600, 86700, 86800, 86900, 87000, 87100, 87200, 87300, 87400, 87500, 87600, 87700, 87800, 87900, 88000, 88100, 88200, 88300, 88400, 88500, 88600, 88700, 88800, 88900, 89000, 89100, 89200, 89300, 89400, 89500, 89600, 89700, 89800, 89900, 90000, 90100, 90200, 90300, 90400, 90500, 90600, 90700, 90800, 90900, 91000, 91100, 91200, 91300, 91400, 91500, 91600, 91700, 91800, 91900, 92000, 92100, 92200, 92300, 92400, 92500, 92600, 92700, 92800, 92900, 93000, 93100, 93200, 93300, 93400, 93500, 93600, 93700, 93800, 93900, 94000, 94100, 94200, 94300, 94400, 94500, 94600, 94700, 94800, 94900, 95000, 95100, 95200, 95300, 95400, 95500, 95600, 95700, 95800, 95900, 96000, 96100, 96200, 96300, 96400, 96500, 96600, 96700, 96800, 96900, 97000, 97100, 97200, 97300, 97400, 97500, 97600, 97700, 97800, 97900, 98000, 98100, 98200, 98300, 98400, 98500, 98600, 98700, 98800, 98900, 99000, 99100, 99200, 99300, 99400, 99500, 99600, 99700, 99800, 99900, 100000]
do2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 13300, 13400, 13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100, 15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900, 16000, 16100, 16200, 16300, 16400, 16500, 16600, 16700, 16800, 16900, 17000, 17100, 17200, 17300, 17400, 17500, 17600, 17700, 17800, 17900, 18000, 18100, 18200, 18300, 18400, 18500, 18600, 18700, 18800, 18900, 19000, 19100, 19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000, 20100, 20200, 20300, 20400, 20500, 20600, 20700, 20800, 20900, 21000, 21100, 21200, 21300, 21400, 21500, 21600, 21700, 21800, 21900, 22000, 22100, 22200, 22300, 22400, 22500, 22600, 22700, 22800, 22900, 23000, 23100, 23200, 23300, 23400, 23500, 23600, 23700, 23800, 23900, 24000, 24100, 24200, 24300, 24400, 24500, 24600, 24700, 24800, 24900, 25000, 25100, 25200, 25300, 25400, 25500, 25600, 25700, 25800, 25900, 26000, 26100, 26200, 26300, 26400, 26500, 26600, 26700, 26800, 26900, 27000, 27100, 27200, 27300, 27400, 27500, 27600, 27700, 27800, 27900, 28000, 28100, 28200, 28300, 28400, 28500, 28600, 28700, 28800, 28900, 29000, 29100, 29200, 29300, 29400, 29500, 29600, 29700, 29800, 29900, 30000, 30100, 30200, 30300, 30400, 30500, 30600, 30700, 30800, 30900, 31000, 31100, 31200, 31300, 31400, 31500, 31600, 31700, 31800, 31900, 32000, 32100, 32200, 32300, 32400, 32500, 32600, 32700, 32800, 32900, 33000, 33100, 33200, 33300, 33400, 33500, 33600, 33700, 33800, 33900, 34000, 34100, 34200, 34300, 34400, 34500, 34600, 34700, 34800, 34900, 35000, 35100, 35200, 35300, 35400, 35500, 35600, 35700, 35800, 35900, 36000, 36100, 36200, 36300, 36400, 36500, 36600, 36700, 36800, 36900, 37000, 37100, 37200, 37300, 37400, 37500, 37600, 37700, 37800, 37900, 38000, 38100, 38200, 38300, 38400, 38500, 38600, 38700, 38800, 38900, 39000, 39100, 39200, 39300, 39400, 39500, 39600, 39700, 39800, 39900, 40000, 40100, 40200, 40300, 40400, 40500, 40600, 40700, 40800, 40900, 41000, 41100, 41200, 41300, 41400, 41500, 41600, 41700, 41800, 41900, 42000, 42100, 42200, 42300, 42400, 42500, 42600, 42700, 42800, 42900, 43000, 43100, 43200, 43300, 43400, 43500, 43600, 43700, 43800, 43900, 44000, 44100, 44200, 44300, 44400, 44500, 44600, 44700, 44800, 44900, 45000, 45100, 45200, 45300, 45400, 45500, 45600, 45700, 45800, 45900, 46000, 46100, 46200, 46300, 46400, 46500, 46600, 46700, 46800, 46900, 47000, 47100, 47200, 47300, 47400, 47500, 47600, 47700, 47800, 47900, 48000, 48100, 48200, 48300, 48400, 48500, 48600, 48700, 48800, 48900, 49000, 49100, 49200, 49300, 49400, 49500, 49600, 49700, 49800, 49900, 50000, 50100, 50200, 50300, 50400, 50500, 50600, 50700, 50800, 50900, 51000, 51100, 51200, 51300, 51400, 51500, 51600, 51700, 51800, 51900, 52000, 52100, 52200, 52300, 52400, 52500, 52600, 52700, 52800, 52900, 53000, 53100, 53200, 53300, 53400, 53500, 53600, 53700, 53800, 53900, 54000, 54100, 54200, 54300, 54400, 54500, 54600, 54700, 54800, 54900, 55000, 55100, 55200, 55300, 55400, 55500, 55600, 55700, 55800, 55900, 56000, 56100, 56200, 56300, 56400, 56500, 56600, 56700, 56800, 56900, 57000, 57100, 57200, 57300, 57400, 57500, 57600, 57700, 57800, 57900, 58000, 58100, 58200, 58300, 58400, 58500, 58600, 58700, 58800, 58900, 59000, 59100, 59200, 59300, 59400, 59500, 59600, 59700, 59800, 59900, 60000, 60100, 60200, 60300, 60400, 60500, 60600, 60700, 60800, 60900, 61000, 61100, 61200, 61300, 61400, 61500, 61600, 61700, 61800, 61900, 62000, 62100, 62200, 62300, 62400, 62500, 62600, 62700, 62800, 62900, 63000, 63100, 63200, 63300, 63400, 63500, 63600, 63700, 63800, 63900, 64000, 64100, 64200, 64300, 64400, 64500, 64600, 64700, 64800, 64900, 65000, 65100, 65200, 65300, 65400, 65500, 65600, 65700, 65800, 65900, 66000, 66100, 66200, 66300, 66400, 66500, 66600, 66700, 66800, 66900, 67000, 67100, 67200, 67300, 67400, 67500, 67600, 67700, 67800, 67900, 68000, 68100, 68200, 68300, 68400, 68500, 68600, 68700, 68800, 68900, 69000, 69100, 69200, 69300, 69400, 69500, 69600, 69700, 69800, 69900, 70000, 70100, 70200, 70300, 70400, 70500, 70600, 70700, 70800, 70900, 71000, 71100, 71200, 71300, 71400, 71500, 71600, 71700, 71800, 71900, 72000, 72100, 72200, 72300, 72400, 72500, 72600, 72700, 72800, 72900, 73000, 73100, 73200, 73300, 73400, 73500, 73600, 73700, 73800, 73900, 74000, 74100, 74200, 74300, 74400, 74500, 74600, 74700, 74800, 74900, 75000, 75100, 75200, 75300, 75400, 75500, 75600, 75700, 75800, 75900, 76000, 76100, 76200, 76300, 76400, 76500, 76600, 76700, 76800, 76900, 77000, 77100, 77200, 77300, 77400, 77500, 77600, 77700, 77800, 77900, 78000, 78100, 78200, 78300, 78400, 78500, 78600, 78700, 78800, 78900, 79000, 79100, 79200, 79300, 79400, 79500, 79600, 79700, 79800, 79900, 80000, 80100, 80200, 80300, 80400, 80500, 80600, 80700, 80800, 80900, 81000, 81100, 81200, 81300, 81400, 81500, 81600, 81700, 81800, 81900, 82000, 82100, 82200, 82300, 82400, 82500, 82600, 82700, 82800, 82900, 83000, 83100, 83200, 83300, 83400, 83500, 83600, 83700, 83800, 83900, 84000, 84100, 84200, 84300, 84400, 84500, 84600, 84700, 84800, 84900, 85000, 85100, 85200, 85300, 85400, 85500, 85600, 85700, 85800, 85900, 86000, 86100, 86200, 86300, 86400, 86500, 86600, 86700, 86800, 86900, 87000, 87100, 87200, 87300, 87400, 87500, 87600, 87700, 87800, 87900, 88000, 88100, 88200, 88300, 88400, 88500, 88600, 88700, 88800, 88900, 89000, 89100, 89200, 89300, 89400, 89500, 89600, 89700, 89800, 89900, 90000, 90100, 90200, 90300, 90400, 90500, 90600, 90700, 90800, 90900, 91000, 91100, 91200, 91300, 91400, 91500, 91600, 91700, 91800, 91900, 92000, 92100, 92200, 92300, 92400, 92500, 92600, 92700, 92800, 92900, 93000, 93100, 93200, 93300, 93400, 93500, 93600, 93700, 93800, 93900, 94000, 94100, 94200, 94300, 94400, 94500, 94600, 94700, 94800, 94900, 95000, 95100, 95200, 95300, 95400, 95500, 95600, 95700, 95800, 95900, 96000, 96100, 96200, 96300, 96400, 96500, 96600, 96700, 96800, 96900, 97000, 97100, 97200, 97300, 97400, 97500, 97600, 97700, 97800, 97900, 98000, 98100, 98200, 98300, 98400, 98500, 98600, 98700, 98800, 98900, 99000, 99100, 99200, 99300, 99400, 99500, 99600, 99700, 99800, 99900, 100000, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000, 10200, 10400, 10600, 10800, 11000, 11200, 11400, 11600, 11800, 12000, 12200, 12400, 12600, 12800, 13000, 13200, 13400, 13600, 13800, 14000, 14200, 14400, 14600, 14800, 15000, 15200, 15400, 15600, 15800, 16000, 16200, 16400, 16600, 16800, 17000, 17200, 17400, 17600, 17800, 18000, 18200, 18400, 18600, 18800, 19000, 19200, 19400, 19600, 19800, 20000, 20200, 20400, 20600, 20800, 21000, 21200, 21400, 21600, 21800, 22000, 22200, 22400, 22600, 22800, 23000, 23200, 23400, 23600, 23800, 24000, 24200, 24400, 24600, 24800, 25000, 25200, 25400, 25600, 25800, 26000, 26200, 26400, 26600, 26800, 27000, 27200, 27400, 27600, 27800, 28000, 28200, 28400, 28600, 28800, 29000, 29200, 29400, 29600, 29800, 30000, 30200, 30400, 30600, 30800, 31000, 31200, 31400, 31600, 31800, 32000, 32200, 32400, 32600, 32800, 33000, 33200, 33400, 33600, 33800, 34000, 34200, 34400, 34600, 34800, 35000, 35200, 35400, 35600, 35800, 36000, 36200, 36400, 36600, 36800, 37000, 37200, 37400, 37600, 37800, 38000, 38200, 38400, 38600, 38800, 39000, 39200, 39400, 39600, 39800, 40000, 40200, 40400, 40600, 40800, 41000, 41200, 41400, 41600, 41800, 42000, 42200, 42400, 42600, 42800, 43000, 43200, 43400, 43600, 43800, 44000, 44200, 44400, 44600, 44800, 45000, 45200, 45400, 45600, 45800, 46000, 46200, 46400, 46600, 46800, 47000, 47200, 47400, 47600, 47800, 48000, 48200, 48400, 48600, 48800, 49000, 49200, 49400, 49600, 49800, 50000, 50200, 50400, 50600, 50800, 51000, 51200, 51400, 51600, 51800, 52000, 52200, 52400, 52600, 52800, 53000, 53200, 53400, 53600, 53800, 54000, 54200, 54400, 54600, 54800, 55000, 55200, 55400, 55600, 55800, 56000, 56200, 56400, 56600, 56800, 57000, 57200, 57400, 57600, 57800, 58000, 58200, 58400, 58600, 58800, 59000, 59200, 59400, 59600, 59800, 60000, 60200, 60400, 60600, 60800, 61000, 61200, 61400, 61600, 61800, 62000, 62200, 62400, 62600, 62800, 63000, 63200, 63400, 63600, 63800, 64000, 64200, 64400, 64600, 64800, 65000, 65200, 65400, 65600, 65800, 66000, 66200, 66400, 66600, 66800, 67000, 67200, 67400, 67600, 67800, 68000, 68200, 68400, 68600, 68800, 69000, 69200, 69400, 69600, 69800, 70000, 70200, 70400, 70600, 70800, 71000, 71200, 71400, 71600, 71800, 72000, 72200, 72400, 72600, 72800, 73000, 73200, 73400, 73600, 73800, 74000, 74200, 74400, 74600, 74800, 75000, 75200, 75400, 75600, 75800, 76000, 76200, 76400, 76600, 76800, 77000, 77200, 77400, 77600, 77800, 78000, 78200, 78400, 78600, 78800, 79000, 79200, 79400, 79600, 79800, 80000, 80200, 80400, 80600, 80800, 81000, 81200, 81400, 81600, 81800, 82000, 82200, 82400, 82600, 82800, 83000, 83200, 83400, 83600, 83800, 84000, 84200, 84400, 84600, 84800, 85000, 85200, 85400, 85600, 85800, 86000, 86200, 86400, 86600, 86800, 87000, 87200, 87400, 87600, 87800, 88000, 88200, 88400, 88600, 88800, 89000, 89200, 89400, 89600, 89800, 90000, 90200, 90400, 90600, 90800, 91000, 91200, 91400, 91600, 91800, 92000, 92200, 92400, 92600, 92800, 93000, 93200, 93400, 93600, 93800, 94000, 94200, 94400, 94600, 94800, 95000, 95200, 95400, 95600, 95800, 96000, 96200, 96400, 96600, 96800, 97000, 97200, 97400, 97600, 97800, 98000, 98200, 98400, 98600, 98800, 99000, 99200, 99400, 99600, 99800, 100000, 100200, 100400, 100600, 100800, 101000, 101200, 101400, 101600, 101800, 102000, 102200, 102400, 102600, 102800, 103000, 103200, 103400, 103600, 103800, 104000, 104200, 104400, 104600, 104800, 105000, 105200, 105400, 105600, 105800, 106000, 106200, 106400, 106600, 106800, 107000, 107200, 107400, 107600, 107800, 108000, 108200, 108400, 108600, 108800, 109000, 109200, 109400, 109600, 109800, 110000, 110200, 110400, 110600, 110800, 111000, 111200, 111400, 111600, 111800, 112000, 112200, 112400, 112600, 112800, 113000, 113200, 113400, 113600, 113800, 114000, 114200, 114400, 114600, 114800, 115000, 115200, 115400, 115600, 115800, 116000, 116200, 116400, 116600, 116800, 117000, 117200, 117400, 117600, 117800, 118000, 118200, 118400, 118600, 118800, 119000, 119200, 119400, 119600, 119800, 120000, 120200, 120400, 120600, 120800, 121000, 121200, 121400, 121600, 121800, 122000, 122200, 122400, 122600, 122800, 123000, 123200, 123400, 123600, 123800, 124000, 124200, 124400, 124600, 124800, 125000, 125200, 125400, 125600, 125800, 126000, 126200, 126400, 126600, 126800, 127000, 127200, 127400, 127600, 127800, 128000, 128200, 128400, 128600, 128800, 129000, 129200, 129400, 129600, 129800, 130000, 130200, 130400, 130600, 130800, 131000, 131200, 131400, 131600, 131800, 132000, 132200, 132400, 132600, 132800, 133000, 133200, 133400, 133600, 133800, 134000, 134200, 134400, 134600, 134800, 135000, 135200, 135400, 135600, 135800, 136000, 136200, 136400, 136600, 136800, 137000, 137200, 137400, 137600, 137800, 138000, 138200, 138400, 138600, 138800, 139000, 139200, 139400, 139600, 139800, 140000, 140200, 140400, 140600, 140800, 141000, 141200, 141400, 141600, 141800, 142000, 142200, 142400, 142600, 142800, 143000, 143200, 143400, 143600, 143800, 144000, 144200, 144400, 144600, 144800, 145000, 145200, 145400, 145600, 145800, 146000, 146200, 146400, 146600, 146800, 147000, 147200, 147400, 147600, 147800, 148000, 148200, 148400, 148600, 148800, 149000, 149200, 149400, 149600, 149800, 150000, 150200, 150400, 150600, 150800, 151000, 151200, 151400, 151600, 151800, 152000, 152200, 152400, 152600, 152800, 153000, 153200, 153400, 153600, 153800, 154000, 154200, 154400, 154600, 154800, 155000, 155200, 155400, 155600, 155800, 156000, 156200, 156400, 156600, 156800, 157000, 157200, 157400, 157600, 157800, 158000, 158200, 158400, 158600, 158800, 159000, 159200, 159400, 159600, 159800, 160000, 160200, 160400, 160600, 160800, 161000, 161200, 161400, 161600, 161800, 162000, 162200, 162400, 162600, 162800, 163000, 163200, 163400, 163600, 163800, 164000, 164200, 164400, 164600, 164800, 165000, 165200, 165400, 165600, 165800, 166000, 166200, 166400, 166600, 166800, 167000, 167200, 167400, 167600, 167800, 168000, 168200, 168400, 168600, 168800, 169000, 169200, 169400, 169600, 169800, 170000, 170200, 170400, 170600, 170800, 171000, 171200, 171400, 171600, 171800, 172000, 172200, 172400, 172600, 172800, 173000, 173200, 173400, 173600, 173800, 174000, 174200, 174400, 174600, 174800, 175000, 175200, 175400, 175600, 175800, 176000, 176200, 176400, 176600, 176800, 177000, 177200, 177400, 177600, 177800, 178000, 178200, 178400, 178600, 178800, 179000, 179200, 179400, 179600, 179800, 180000, 180200, 180400, 180600, 180800, 181000, 181200, 181400, 181600, 181800, 182000, 182200, 182400, 182600, 182800, 183000, 183200, 183400, 183600, 183800, 184000, 184200, 184400, 184600, 184800, 185000, 185200, 185400, 185600, 185800, 186000, 186200, 186400, 186600, 186800, 187000, 187200, 187400, 187600, 187800, 188000, 188200, 188400, 188600, 188800, 189000, 189200, 189400, 189600, 189800, 190000, 190200, 190400, 190600, 190800, 191000, 191200, 191400, 191600, 191800, 192000, 192200, 192400, 192600, 192800, 193000, 193200, 193400, 193600, 193800, 194000, 194200, 194400, 194600, 194800, 195000, 195200, 195400, 195600, 195800, 196000, 196200, 196400, 196600, 196800, 197000, 197200, 197400, 197600, 197800, 198000, 198200, 198400, 198600, 198800, 199000, 199200, 199400, 199600, 199800, 200000]
for a1 in open('listvideo.txt').read().splitlines():
    i = 99
    i2 = 0
    for a in open(a1).read().splitlines():
        i += 1
        if i == 100:
            f1 = open(a1.replace('.html', '') + '_page_' + str(i2 + 1) + '.html', 'a+')
            f1.write("<!DOCTYPE html><html>        <style>            li {  color: white;  font-family: sans-serif;  font-size:1.5vw;}			body { background-color: #303030;}        </style>	<head>		<title>memes archive</title>	</head>	</body style='background-color:#33475b'>	<p><span style='font-size: 14pt; color: #ecf0f1;'><strong>Made For https://bakchodi.org</strong></span></p><ol>")
        if i in do:
            i2 += 1
            fa = open(a1.replace('.html', '') + '_page_' + str(i2 + 1) + '.html', 'a+')
            fa.write("<!DOCTYPE html><html>        <style>            li {  color: white;  font-family: sans-serif;  font-size:1.5vw;}			body { background-color: #303030;}        </style>	<head>		<title>memes archive</title>	</head>	</body style='background-color:#33475b'>	<p><span style='font-size: 14pt; color: #ecf0f1;'><strong>Made For https://bakchodi.org</strong></span></p><ol>")
            f5 = open('index-page.txt', 'a+')
            f5.write('index_' + a1.replace('.html', '') + '_page_' + str(i2) + '.html\n')
            if i != 100:
                f2 = open(a1.replace('.html', '') + '_page_' + str(i2) + '.html', 'a+')
                f2.write("</ol>")
        if i > 99:
            f4 = open(a1.replace('.html', '') + '_page_' + str(i2) + '.html', 'a+')
            f4.write("      " + a + '\n')
        
# for a1 in open('index-page.txt').read().splitlines():
#     f4 = open('index2.html', 'a+')
#     f4.write("<li><a href='" + a1 + "'><span style='font-family: 'andale mono', monospace;'><strong>" + a1 + "</strong></span> </a></li>")
#     print("<li><a href='" + a1 + "'><span style='font-family: 'andale mono', monospace;'><strong>" + a1 + "</strong></span> </a></li>")
#        print("<html lang='en'>\n  <link rel='stylesheet' href='style.css' />\n  <head>\n    <meta charset='utf-8' />\n\n    <title>Memes Gallery</title>\n    <meta name='description' content='collection of Memes' />\n    <meta name='author' content='Rishabh' />\n\n    <style type='text/css'></style>\n  </head>\n  <body>\n    <div id='gallery'>\n")
# print("<html lang='en'>\n  <link rel='stylesheet' href='style.css' />\n  <head>\n    <meta charset='utf-8' />\n\n    <title>Memes Gallery</title>\n    <meta name='description' content='collection of Memes' />\n    <meta name='author' content='Rishabh' />\n\n    <style type='text/css'></style>\n  </head>\n  <body>\n    <div id='gallery'>\n"  "\n    </div>\n  </body>\n</html>")
# for a in range(1, 1000):
#     i += 1
#     do.append(i*200)
# print(do2)
    