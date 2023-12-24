from xtquant import xtdata
from crazy import *
import time
def on_progress(data):
	print(data)
#xtdata.download_history_data2(stock_list=['600791.SH', '600989.SH', '002714.SZ'], period='tick', start_time='20231218', end_time='20231218', callback=on_progress)

res = xtdata.get_market_data(stock_list=['002714.SZ', '600989.SH', '002714.SZ'], period='tick', start_time='20221111', end_time='20231218')

# dict = [{'20231222': ['600303.SH', '603389.SH', '000669.SZ', '603608.SH', '002748.SZ', '002494.SZ', '002615.SZ', '002613.SZ']}, {'20231221': ['603007.SH', '600421.SH', '603103.SH', '002697.SZ', '603389.SH', '000669.SZ', '001239.SZ', '002615.SZ', '002952.SZ']}, {'20231220': ['000669.SZ', '300949.SZ', '600666.SH', '600692.SH', '002089.SZ', '603789.SH', '001239.SZ', '002915.SZ']}, {'20231219': ['603967.SH', '601022.SH', '002862.SZ', '000669.SZ', '002564.SZ', '002682.SZ', '600666.SH', '600630.SH', '300949.SZ', '002089.SZ']}, {'20231218': ['600358.SH', '002591.SZ', '603230.SH', '603721.SH', '600234.SH', '002875.SZ', '600647.SH', '300949.SZ', '603789.SH']}, {'20231215': ['600712.SH', '603230.SH', '600725.SH', '000524.SZ', '600149.SH', '600647.SH', '002445.SZ', '605488.SH', '600579.SH', '600791.SH']}, {'20231214': ['603066.SH', '000919.SZ', '600712.SH', '002989.SZ', '002893.SZ', '600647.SH', '603660.SH', '600807.SH', '600579.SH']}, {'20231213': ['600712.SH', '603660.SH', '600083.SH', '002739.SZ', '688506.SH', '600807.SH']}, {'20231212': ['600715.SH', '430198.BJ', '600712.SH', '603729.SH', '002021.SZ', '603660.SH', '600083.SH', '688506.SH']}, {'20231211': ['430198.BJ', '873001.BJ', '002021.SZ', '603660.SH']}, {'20231208': ['600715.SH', '603038.SH', '430564.BJ', '002021.SZ', '600678.SH', '002510.SZ', '603660.SH', '832145.BJ', '603466.SH', '603153.SH', '603189.SH']}, {'20231207': ['600715.SH', '000802.SZ', '002021.SZ', '002451.SZ', '600678.SH', '600302.SH', '002510.SZ', '603725.SH', '600571.SH', '600981.SH']}, {'20231206': ['600250.SH', '002451.SZ', '605179.SH', '600647.SH', '002510.SZ', '600981.SH']}, {'20231205': ['600250.SH', '600078.SH', '000757.SZ', '605289.SH', '000903.SZ', '603860.SH', '600647.SH', '600444.SH', '300560.SZ', '600571.SH']}, {'20231204': ['600250.SH', '600228.SH', '603721.SH', '000868.SZ', '603860.SH', '600647.SH', '600571.SH', '603189.SH', '600661.SH']}, {'20231201': ['600250.SH', '603023.SH', '600647.SH', '002927.SZ', '600571.SH']}, {'20231130': ['600250.SH', '002031.SZ', '603211.SH', '600647.SH', '002927.SZ', '002952.SZ']}, {'20231129': ['605228.SH', '000903.SZ', '300351.SZ', '603211.SH', '600523.SH', '603006.SH', '600647.SH', '002331.SZ', '603557.SH', '836221.BJ', '301013.SZ', '600178.SH']}, {'20231128': ['002058.SZ', '600589.SH', '605005.SH', '605289.SH', '600647.SH', '600178.SH']}, {'20231127': ['600698.SH', '836247.BJ', '834407.BJ', '600589.SH', '600513.SH', '603536.SH', '002021.SZ', '600647.SH', '000518.SZ', '002355.SZ', '831195.BJ', '603286.SH', '000625.SZ', '600178.SH']}, {'20231124': ['600159.SH', '300697.SZ', '000670.SZ', '002331.SZ', '000518.SZ', '002416.SZ', '002776.SZ', '603286.SH', '600178.SH', '600766.SH']}, {'20231123': ['002275.SZ', '605577.SH', '600589.SH', '832171.BJ', '603598.SH', '000670.SZ', '002564.SZ', '600053.SH', '603178.SH', '603488.SH', '002712.SZ', '000518.SZ', '002416.SZ', '000710.SZ', '002137.SZ', '600766.SH']}, {'20231122': ['000863.SZ', '002561.SZ', '600658.SH', '600159.SH', '603663.SH', '603586.SH', '603598.SH', '000669.SZ', '002564.SZ', '603488.SH', '603499.SH', '000510.SZ', '000006.SZ']}, {'20231121': ['000863.SZ', '600658.SH', '002786.SZ', '300288.SZ', '603586.SH', '603021.SH', '002564.SZ', '603488.SH', '002559.SZ', '600455.SH', '002195.SZ']}, {'20231120': ['000863.SZ', '600658.SH', '002103.SZ', '002786.SZ', '000669.SZ', '603488.SH', '600775.SH', '002559.SZ']}, {'20231117': ['002569.SZ', '002103.SZ', '001300.SZ', '000669.SZ', '300242.SZ', '603838.SH', '600738.SH', '600775.SH', '002239.SZ']}, {'20231116': ['002569.SZ', '002786.SZ', '001300.SZ', '002564.SZ', '600753.SH', '002141.SZ', '605086.SH', '600775.SH', '001319.SZ', '603037.SH', '002239.SZ']}, {'20231115': ['003032.SZ', '603002.SH', '603496.SH', '002178.SZ', '002512.SZ', '000056.SZ', '605086.SH', '603528.SH']}, {'20231114': ['003032.SZ', '600119.SH', '601022.SH', '000697.SZ', '600462.SH', '605086.SH', '002988.SZ', '603528.SH']}, {'20231113': ['003032.SZ', '600119.SH', '600306.SH', '000615.SZ', '601022.SH', '001300.SZ', '000697.SZ', '000056.SZ', '605086.SH', '600178.SH']}, {'20231110': ['002238.SZ', '000697.SZ', '603816.SH', '603320.SH', '000056.SZ', '605050.SH', '600178.SH', '605255.SH']}, {'20231109': ['600470.SH', '002238.SZ', '600679.SH', '000697.SZ', '001314.SZ', '000056.SZ', '002988.SZ', '002584.SZ', '605255.SH', '605218.SH']}, {'20231108': ['600470.SH', '002238.SZ', '600679.SH', '002136.SZ', '000828.SZ', '603390.SH', '603266.SH', '000056.SZ', '002988.SZ', '600592.SH', '605218.SH']}, {'20231107': ['603158.SH', '002238.SZ', '603729.SH', '000955.SZ', '000828.SZ', '603390.SH', '603266.SH', '002313.SZ', '603380.SH', '002988.SZ', '603037.SH', '600816.SH', '600592.SH']}, {'20231106': ['002238.SZ', '002031.SZ', '000955.SZ', '603603.SH', '002981.SZ', '603390.SH', '002592.SZ', '603266.SH', '002284.SZ', '000711.SZ', '002313.SZ', '002931.SZ', '000046.SZ', '600592.SH']}, {'20231103': ['002313.SZ', '002692.SZ', '002976.SZ', '600592.SH', '002031.SZ', '603390.SH', '002009.SZ', '000046.SZ', '603266.SH']}, {'20231102': ['000615.SZ', '002898.SZ', '002981.SZ', '002592.SZ', '002277.SZ', '002692.SZ', '600816.SH', '000628.SZ']}, {'20231101': ['300588.SZ', '002592.SZ', '002277.SZ', '002692.SZ', '600816.SH', '000628.SZ', '002800.SZ']}, {'20231031': ['603890.SH', '002437.SZ', '000676.SZ', '002592.SZ', '002277.SZ', '603266.SH', '603332.SH', '000021.SZ', '000892.SZ', '603283.SH', '603929.SH', '600816.SH', '000628.SZ', '603559.SH']}, {'20231030': ['603338.SH', '603629.SH', '002437.SZ', '000676.SZ', '002232.SZ', '603266.SH', '000796.SZ', '002564.SZ', '002457.SZ', '603788.SH', '603929.SH', '000628.SZ', '600418.SH']}, {'20231027': ['002699.SZ', '600589.SH', '603768.SH', '002232.SZ', '603266.SH', '002564.SZ', '002682.SZ', '002671.SZ', '301151.SZ', '603788.SH', '600853.SH', '001319.SZ', '603929.SH', '000628.SZ', '600418.SH']}, {'20231026': ['002991.SZ', '002205.SZ', '002682.SZ', '003039.SZ', '002671.SZ', '301151.SZ', '002457.SZ', '603788.SH', '000525.SZ', '000628.SZ', '002771.SZ', '300262.SZ']}, {'20231025': ['002827.SZ', '000631.SZ', '002205.SZ', '603856.SH', '603176.SH', '600239.SH', '600283.SH', '301038.SZ', '002443.SZ', '002682.SZ', '003039.SZ', '002671.SZ', '002586.SZ', '301151.SZ', '002457.SZ', '301519.SZ', '603788.SH', '600510.SH', '000010.SZ', '600735.SH', '000628.SZ', '603969.SH', '603985.SH', '603616.SH']}, {'20231024': ['600520.SH', '000608.SZ', '002682.SZ', '603788.SH', '600510.SH', '000628.SZ', '002771.SZ', '603388.SH', '603985.SH']}, {'20231023': ['600520.SH', '603399.SH', '000711.SZ', '600666.SH', '000628.SZ']}, {'20231020': ['600520.SH', '000757.SZ', '600666.SH', '000410.SZ', '000628.SZ']}, {'20231019': ['600599.SH', '000628.SZ', '002771.SZ']}, {'20231018': ['600520.SH', '600599.SH', '600666.SH', '002729.SZ', '600439.SH', '002771.SZ']}, {'20231017': ['002569.SZ', '300180.SZ', '600599.SH', '000007.SZ', '603168.SH', '002771.SZ']}, {'20231016': ['603276.SH', '600721.SH', '002569.SZ', '600589.SH', '002387.SZ', '603139.SH', '600599.SH', '603036.SH', '603178.SH', '002708.SZ', '002286.SZ', '603168.SH', '000752.SZ', '000727.SZ']}, {'20231013': ['600721.SH', '002569.SZ', '600396.SH', '002708.SZ', '603168.SH']}, {'20231012': ['600721.SH', '002569.SZ', '603163.SH', '600895.SH', '603168.SH', '002456.SZ', '000541.SZ']}, {'20231011': ['002569.SZ', '002514.SZ', '603178.SH', '002456.SZ', '002535.SZ', '000541.SZ']}, {'20231010': ['002569.SZ', '600589.SH', '002514.SZ', '300351.SZ', '603178.SH', '002005.SZ', '001298.SZ', '002456.SZ']}, {'20231009': ['002569.SZ', '600589.SH', '002514.SZ', '603496.SH', '601127.SH', '300351.SZ', '002922.SZ', '603178.SH', '002456.SZ', '605333.SH', '002369.SZ']}, {'20230928': ['600355.SH', '002786.SZ', '600198.SH', '600545.SH', '000546.SZ', '002535.SZ']}, {'20230927': ['600355.SH', '603895.SH', '002691.SZ', '002433.SZ', '600545.SH', '000546.SZ', '002535.SZ', '603280.SH']}, {'20230926': ['600355.SH', '603895.SH', '002691.SZ']}, {'20230925': ['600355.SH', '002892.SZ', '603496.SH', '001282.SZ', '603083.SH', '600365.SH', '002848.SZ']}, {'20230922': ['000996.SZ', '001282.SZ', '002021.SZ', '002742.SZ', '600759.SH', '002776.SZ', '000752.SZ', '600365.SH']}, {'20230921': ['600355.SH', '000996.SZ', '002742.SZ']}, {'20230920': ['000996.SZ', '002021.SZ', '001319.SZ', '000752.SZ']}, {'20230919': ['600671.SH', '000996.SZ', '002021.SZ', '001319.SZ', '605333.SH']}, {'20230918': ['600172.SH', '000996.SZ', '002889.SZ', '002021.SZ', '000962.SZ', '000752.SZ']}, {'20230915': ['600408.SH', '000996.SZ', '002194.SZ', '002248.SZ', '000752.SZ']}, {'20230914': ['301419.SZ', '002886.SZ', '605365.SH', '002194.SZ', '003016.SZ', '002792.SZ', '000752.SZ', '600823.SH']}, {'20230913': ['600802.SH', '605365.SH', '003016.SZ', '300300.SZ', '000592.SZ', '600823.SH']}, {'20230912': ['600520.SH', '603023.SH', '603887.SH', '000752.SZ', '002970.SZ', '603815.SH']}, {'20230911': ['600303.SH', '603626.SH', '002642.SZ', '605588.SH', '000752.SZ', '001268.SZ', '002767.SZ']}, {'20230908': ['600589.SH', '603221.SH', '605588.SH', '001268.SZ', '002767.SZ']}, {'20230907': ['600589.SH', '002855.SZ', '603226.SH', '600892.SH', '605588.SH']}, {'20230906': ['600792.SH', '002795.SZ']}, {'20230905': ['002855.SZ', '603326.SH', '000046.SZ', '002776.SZ', '002861.SZ']}, {'20230904': ['002855.SZ', '002822.SZ', '603326.SH', '600792.SH', '603161.SH', '600540.SH', '002776.SZ']}, {'20230901': ['603326.SH', '000046.SZ', '002776.SZ']}, {'20230831': ['002855.SZ', '600530.SH', '600336.SH']}, {'20230830': ['002699.SZ', '002855.SZ', '688191.SH', '600753.SH', '603767.SH', '002833.SZ']}, {'20230829': ['600684.SH']}, {'20230828': ['603555.SH', '600683.SH', '000609.SZ', '300561.SZ', '002926.SZ', '601108.SH', '603806.SH', '603106.SH', '000712.SZ', '601788.SH', '601136.SH', '600322.SH', '600030.SH', '300803.SZ', '601878.SH', '000514.SZ', '000996.SZ', '600318.SH', '600643.SH', '600290.SH', '600289.SH', '002670.SZ', '000828.SZ', '600369.SH', '601901.SH', '301315.SZ', '300169.SZ', '603828.SH', '000850.SZ', '600684.SH', '002673.SZ', '000166.SZ', '600109.SH', '600864.SH', '603307.SH', '000971.SZ', '601688.SH', '002865.SZ', '002949.SZ', '601555.SH', '603117.SH', '002500.SZ', '688318.SH', '001366.SZ', '600257.SH', '601099.SH', '601456.SH', '300941.SZ', '600155.SH', '000728.SZ', '601059.SH', '601066.SH', '601375.SH', '002736.SZ', '601995.SH', '000416.SZ', '601236.SH', '002177.SZ', '830799.BJ', '000623.SZ', '000750.SZ', '000620.SZ', '002797.SZ', '002802.SZ', '002939.SZ', '600837.SH', '603383.SH', '600570.SH', '600999.SH', '600095.SH', '600918.SH', '600906.SH', '601528.SH', '000783.SZ', '601519.SH', '000656.SZ', '000046.SZ', '600881.SH', '300295.SZ', '601696.SH', '000987.SZ', '600909.SH', '002333.SZ', '600621.SH', '002945.SZ', '600191.SH', '600823.SH', '600446.SH', '002305.SZ', '000686.SZ', '601162.SH']}, {'20230825': ['600589.SH', '600257.SH', '000546.SZ']}, {'20230824': ['600589.SH', '605398.SH', '603220.SH']}, {'20230823': ['301159.SZ', '605398.SH', '603159.SH']}, {'20230822': ['600671.SH', '002229.SZ', '000826.SZ', '002309.SZ', '605398.SH', '002087.SZ', '002279.SZ']}, {'20230821': ['600671.SH', '603162.SH']}, {'20230818': ['001324.SZ', '000995.SZ', '002527.SZ', '000046.SZ', '688671.SH']}, {'20230817': ['000982.SZ', '002433.SZ', '002927.SZ', '000046.SZ']}, {'20230816': ['002569.SZ', '000615.SZ', '000971.SZ', '600462.SH', '002433.SZ', '000046.SZ']}, {'20230815': ['000615.SZ', '001324.SZ', '002433.SZ', '000046.SZ', '000752.SZ']}, {'20230814': ['002451.SZ', '002433.SZ', '000752.SZ']}, {'20230811': ['600322.SH', '603778.SH', '002433.SZ', '000620.SZ', '000006.SZ', '000752.SZ']}, {'20230810': ['603716.SH', '600530.SH', '000903.SZ', '603778.SH', '301448.SZ', '002433.SZ', '000620.SZ', '000046.SZ']}, {'20230809': ['600530.SH', '002157.SZ', '600613.SH', '002787.SZ', '000620.SZ']}, {'20230808': ['002086.SZ', '600530.SH', '002157.SZ', '000620.SZ']}, {'20230807': ['603106.SH', '002157.SZ', '002564.SZ']}, {'20230804': ['600239.SH', '603536.SH', '601456.SH']}, {'20230803': ['603038.SH', '600239.SH', '601456.SH', '600906.SH']}, {'20230802': ['000890.SZ', '600239.SH', '600361.SH', '600734.SH', '600468.SH', '600595.SH']}, {'20230801': ['000971.SZ', '002377.SZ', '600734.SH', '601007.SH']}, {'20230731': ['300169.SZ', '000850.SZ', '000971.SZ', '002377.SZ', '601099.SH', '600155.SH', '600266.SH', '003043.SZ', '603116.SH', '600823.SH', '601162.SH']}, {'20230728': ['002671.SZ']}, {'20230727': ['603682.SH', '000572.SZ', '603023.SH', '002666.SZ', '002196.SZ', '002575.SZ', '603786.SH', '600823.SH', '002662.SZ']}, {'20230726': ['603682.SH', '600743.SH', '603828.SH', '601099.SH', '002575.SZ', '000656.SZ', '000752.SZ', '600823.SH']}, {'20230725': ['603682.SH', '603023.SH', '601136.SH', '000408.SZ', '601099.SH', '600936.SH', '000638.SZ', '002482.SZ', '000752.SZ']}, {'20230724': ['600322.SH', '600159.SH', '002310.SZ', '600530.SH', '002157.SZ', '603828.SH', '301365.SZ', '002866.SZ', '000010.SZ', '000752.SZ']}, {'20230721': ['600280.SH', '002310.SZ', '002336.SZ', '605188.SH', '000752.SZ']}, {'20230720': ['002316.SZ', '600280.SH']}, {'20230719': ['002502.SZ', '600135.SH', '600280.SH', '600449.SH']}, {'20230718': ['002502.SZ', '002870.SZ']}, {'20230717': ['002502.SZ', '605196.SH', '000669.SZ', '000004.SZ']}, {'20230714': ['002400.SZ', '000561.SZ', '000004.SZ', '000897.SZ']}, {'20230713': ['002103.SZ', '002526.SZ', '605228.SH', '600719.SH']}, {'20230712': ['000996.SZ', '600540.SH', '002026.SZ', '600719.SH', '600480.SH']}, {'20230711': ['603131.SH', '000996.SZ', '000570.SZ', '002564.SZ', '600719.SH', '600480.SH', '600365.SH']}, {'20230710': ['603023.SH', '000996.SZ', '002893.SZ', '600719.SH', '002976.SZ', '002616.SZ']}, {'20230707': ['000996.SZ', '601567.SH', '600719.SH', '002976.SZ', '002616.SZ']}, {'20230706': ['600826.SH', '000996.SZ', '002428.SZ', '603045.SH', '600719.SH']}, {'20230705': ['002656.SZ', '605005.SH', '000996.SZ', '002428.SZ', '000980.SZ', '603030.SH', '002482.SZ', '600719.SH', '002703.SZ']}, {'20230704': ['600497.SH', '000996.SZ', '002428.SZ', '603030.SH', '000980.SZ', '603045.SH', '000796.SZ', '300489.SZ', '002114.SZ', '000691.SZ', '603355.SH', '600112.SH', '002703.SZ', '002535.SZ']}, {'20230703': ['002037.SZ', '002569.SZ', '000996.SZ', '603030.SH', '000678.SZ', '603178.SH', '000007.SZ', '000046.SZ', '002535.SZ']}, {'20230630': ['002656.SZ', '605318.SH', '002031.SZ', '603030.SH', '603042.SH', '002470.SZ', '000007.SZ', '002286.SZ']}, {'20230629': ['002031.SZ', '603030.SH', '603042.SH', '000678.SZ', '002196.SZ', '603767.SH', '000007.SZ', '002776.SZ']}, {'20230628': ['600776.SH', '000615.SZ', '603042.SH', '000796.SZ', '600491.SH', '000007.SZ', '002740.SZ', '002808.SZ', '600860.SH']}, {'20230627': ['000860.SZ', '600310.SH', '603042.SH', '000796.SZ', '002742.SZ', '002740.SZ', '000037.SZ']}, {'20230626': ['002585.SZ', '603042.SH', '000796.SZ', '603738.SH', '002199.SZ', '002553.SZ']}, {'20230621': ['002585.SZ', '603042.SH', '002553.SZ', '603052.SH', '000790.SZ', '600117.SH']}, {'20230620': ['600388.SH', '600421.SH', '002553.SZ', '603052.SH', '002513.SZ']}, {'20230619': ['600421.SH', '603030.SH', '002896.SZ', '600602.SH', '002513.SZ', '000936.SZ', '002162.SZ', '688071.SH']}, {'20230616': ['002164.SZ', '600589.SH', '002527.SZ', '000151.SZ', '002896.SZ', '000936.SZ', '002535.SZ']}, {'20230615': ['002725.SZ', '000584.SZ', '600589.SH', '002211.SZ', '000936.SZ', '603322.SH', '002535.SZ', '002089.SZ']}, {'20230614': ['600589.SH', '603030.SH', '600601.SH', '603006.SH', '000936.SZ', '002355.SZ', '002740.SZ', '002146.SZ', '002089.SZ']}, {'20230613': ['603335.SH', '600589.SH', '600306.SH', '603030.SH', '002536.SZ', '002177.SZ', '002355.SZ', '002087.SZ', '002146.SZ']}, {'20230612': ['600589.SH', '600306.SH', '001339.SZ', '603268.SH', '002177.SZ', '301013.SZ', '002261.SZ', '603880.SH', '002146.SZ']}, {'20230609': ['600683.SH', '600303.SH', '600589.SH', '001339.SZ', '603779.SH', '000620.SZ', '002776.SZ', '603880.SH', '002146.SZ']}, {'20230608': ['600589.SH', '000005.SZ', '605178.SH', '000971.SZ', '603779.SH', '001314.SZ', '000620.SZ', '002587.SZ']}, {'20230607': ['600589.SH', '002055.SZ', '000005.SZ', '605178.SH', '603108.SH', '000971.SZ', '000711.SZ', '002482.SZ', '000620.SZ']}, {'20230606': ['603629.SH', '002217.SZ', '000615.SZ', '000005.SZ', '000971.SZ', '000711.SZ', '001314.SZ', '600898.SH', '002482.SZ', '000620.SZ', '600136.SH', '000046.SZ']}, {'20230605': ['002902.SZ', '603629.SH', '002482.SZ', '002177.SZ', '000620.SZ', '000046.SZ', '600823.SH']}, {'20230602': ['002902.SZ', '603629.SH', '002632.SZ', '002173.SZ', '002395.SZ', '002021.SZ', '000711.SZ', '605588.SH', '000620.SZ', '000046.SZ', '600823.SH', '002089.SZ']}, {'20230601': ['002502.SZ', '002173.SZ', '002395.SZ', '002021.SZ', '600560.SH', '000711.SZ', '002289.SZ', '000620.SZ', '000888.SZ', '600823.SH']}, {'20230531': ['002173.SZ', '002021.SZ', '600560.SH', '000711.SZ', '605118.SH', '002289.SZ', '603228.SH', '000620.SZ', '603869.SH', '002093.SZ', '600823.SH', '603803.SH']}, {'20230530': ['002173.SZ', '000889.SZ', '002021.SZ', '000620.SZ', '603869.SH', '300753.SZ']}, {'20230529': ['002173.SZ', '002211.SZ', '600283.SH', '000620.SZ', '603869.SH', '001316.SZ']}, {'20230526': ['301041.SZ', '600283.SH', '301038.SZ', '605580.SH', '600982.SH', '600719.SH', '603196.SH', '000620.SZ', '603616.SH']}, {'20230525': ['301041.SZ', '300510.SZ', '603608.SH', '605580.SH', '000004.SZ', '603196.SH', '603933.SH']}, {'20230524': ['000584.SZ', '000615.SZ', '002157.SZ', '000620.SZ', '000046.SZ', '603933.SH', '002808.SZ', '600117.SH']}, {'20230523': ['000584.SZ', '600310.SH', '002157.SZ', '000620.SZ']}, {'20230522': ['300768.SZ', '000584.SZ', '600303.SH', '603030.SH', '002157.SZ', '603196.SH', '000620.SZ', '603933.SH']}, {'20230519': ['603728.SH', '688048.SH', '603196.SH', '301368.SZ', '002689.SZ', '000525.SZ']}, {'20230518': ['002157.SZ', '002153.SZ', '603196.SH', '002087.SZ', '000525.SZ']}, {'20230517': ['603613.SH', '603196.SH', '600375.SH']}, {'20230516': ['603356.SH', '603196.SH']}, {'20230515': ['600811.SH', '000523.SZ', '601999.SH', '000697.SZ', '002721.SZ', '605011.SH', '603790.SH']}, {'20230512': ['000697.SZ', '000892.SZ', '002586.SZ', '002721.SZ', '603790.SH', '603116.SH']}, {'20230511': ['603598.SH', '000697.SZ', '603557.SH', '603790.SH', '600730.SH', '600088.SH']}, {'20230510': ['002712.SZ', '000046.SZ']}, {'20230509': ['600928.SH', '002554.SZ', '601598.SH', '601326.SH', '600636.SH']}, {'20230508': ['600436.SH', '000526.SZ', '002052.SZ', '601326.SH', '600636.SH', '000046.SZ', '002776.SZ', '603357.SH']}, {'20230505': ['600757.SH', '600303.SH', '002485.SZ', '603030.SH', '002052.SZ', '601801.SH', '600229.SH', '601326.SH', '600136.SH', '002776.SZ', '002089.SZ']}, {'20230504': ['600757.SH', '002485.SZ', '002052.SZ', '002555.SZ', '603133.SH', '000004.SZ', '600229.SH', '000571.SZ', '600543.SH', '600518.SH']}, {'20230428': ['002448.SZ', '300108.SZ', '000014.SZ', '603133.SH', '603040.SH', '000056.SZ', '600612.SH', '600136.SH']}, {'20230427': ['600671.SH', '600757.SH', '600589.SH', '002820.SZ', '601699.SH']}, {'20230426': ['603768.SH', '603199.SH', '000571.SZ', '002315.SZ', '002089.SZ']}, {'20230425': ['300573.SZ', '002229.SZ', '600239.SH', '002418.SZ', '002478.SZ', '002089.SZ']}, {'20230424': ['603757.SH']}, {'20230419': ['002343.SZ']}, {'20230418': ['600759.SH']}, {'20230417': ['002852.SZ', '603518.SH', '002959.SZ', '000521.SZ', '000921.SZ']}, {'20230414': ['600706.SH', '600326.SH', '000710.SZ', '002535.SZ']}, {'20230413': ['600373.SH', '002343.SZ', '601921.SH', '002089.SZ']}, {'20230412': ['002052.SZ', '002577.SZ', '002343.SZ']}, {'20230411': ['002772.SZ', '600706.SH']}, {'20230410': ['600405.SH', '002656.SZ', '605168.SH', '002777.SZ', '600306.SH', '002605.SZ', '002122.SZ', '002292.SZ']}, {'20230407': ['002221.SZ', '002665.SZ']}, {'20230406': ['002681.SZ', '603291.SH', '002612.SZ']}, {'20230404': ['603007.SH', '603291.SH', '000809.SZ']}, {'20230403': ['603291.SH', '000021.SZ', '605167.SH', '600182.SH']}, {'20230331': ['002316.SZ', '002052.SZ', '603291.SH']}, {'20230330': ['603291.SH', '002536.SZ']}, {'20230329': ['603291.SH', '000697.SZ', '002184.SZ', '601116.SH', '000059.SZ', '002493.SZ', '000525.SZ']}, {'20230328': ['600346.SH', '603291.SH', '601116.SH', '603225.SH', '002153.SZ', '601233.SH', '002493.SZ']}, {'20230327': ['002410.SZ', '600228.SH', '002229.SZ', '600289.SH', '000697.SZ', '002153.SZ', '002351.SZ', '000158.SZ']}, {'20230324': ['002229.SZ', '002309.SZ']}, {'20230323': ['600303.SH', '600589.SH', '002229.SZ', '603603.SH', '002717.SZ', '603065.SH']}, {'20230322': ['600303.SH', '002229.SZ', '000403.SZ', '300612.SZ', '000564.SZ', '603018.SH', '603065.SH', '002280.SZ']}, {'20230321': ['601121.SH', '000564.SZ', '002740.SZ', '001337.SZ']}, {'20230320': ['601121.SH', '002803.SZ', '603282.SH', '000564.SZ', '600449.SH', '001337.SZ']}, {'20230317': ['601121.SH', '603282.SH', '002358.SZ', '002599.SZ', '002280.SZ', '001337.SZ']}, {'20230316': ['603007.SH', '601121.SH', '603282.SH', '002358.SZ', '001255.SZ', '603153.SH', '001337.SZ']}, {'20230315': ['601121.SH', '600303.SH', '600228.SH', '002771.SZ', '603388.SH', '603153.SH', '001337.SZ']}, {'20230314': ['600228.SH', '001337.SZ', '603153.SH', '601121.SH', '600303.SH', '000065.SZ', '003001.SZ']}, {'20230313': ['001366.SZ', '001337.SZ', '002828.SZ', '601121.SH', '603007.SH', '000065.SZ', '301137.SZ', '600666.SH']}, {'20230310': ['001278.SZ', '001366.SZ', '001337.SZ', '603007.SH', '002089.SZ']}, {'20230309': ['603912.SH', '603007.SH', '001278.SZ', '000890.SZ', '603061.SH', '001366.SZ', '600468.SH', '001337.SZ', '600105.SH', '002089.SZ']}, {'20230308': ['603912.SH', '605398.SH', '603061.SH', '001366.SZ', '001337.SZ', '002089.SZ']}, {'20230307': ['603860.SH', '002796.SZ', '001337.SZ', '002740.SZ', '600666.SH', '603061.SH']}, {'20230306': ['603061.SH', '603860.SH', '600666.SH', '002740.SZ', '601798.SH', '001337.SZ', '002089.SZ']}, {'20230303': ['603042.SH', '600666.SH', '002470.SZ', '603929.SH']}, {'20230302': ['603366.SH', '603042.SH', '600666.SH', '603660.SH', '002740.SZ']}, {'20230301': ['000925.SZ', '603042.SH', '600666.SH', '002089.SZ']}, {'20230228': ['000925.SZ', '601566.SH', '603042.SH', '003016.SZ', '002207.SZ', '600666.SH', '001311.SZ', '002740.SZ', '002808.SZ']}, {'20230227': ['600666.SH']}, {'20230224': ['000532.SZ', '603307.SH', '600666.SH', '002590.SZ']}, {'20230223': ['001260.SZ', '603307.SH', '600666.SH', '603528.SH', '002089.SZ']}, {'20230222': ['603307.SH', '002021.SZ', '603211.SH', '600666.SH']}, {'20230221': ['002086.SZ', '001260.SZ', '603307.SH', '600666.SH', '002104.SZ', '600624.SH']}, {'20230220': ['002086.SZ', '001260.SZ', '603307.SH', '600628.SH', '600666.SH', '002878.SZ', '002047.SZ']}, {'20230217': ['600671.SH', '002086.SZ', '001260.SZ', '002425.SZ', '603307.SH', '002970.SZ']}, {'20230216': ['600449.SH', '600378.SH', '600825.SH']}, {'20230215': ['600666.SH', '600449.SH', '001314.SZ', '600378.SH', '000752.SZ']}, {'20230214': ['000584.SZ', '002229.SZ', '002660.SZ', '605389.SH', '600449.SH', '002792.SZ', '000752.SZ']}, {'20230213': ['000584.SZ', '002951.SZ', '002660.SZ', '605389.SH', '300114.SZ']}, {'20230210': ['000584.SZ', '300114.SZ', '002229.SZ']}, {'20230209': ['000584.SZ', '002328.SZ', '002229.SZ', '601360.SH', '601059.SH', '300114.SZ', '002882.SZ']}, {'20230208': ['600817.SH', '002229.SZ', '002813.SZ', '601360.SH', '002577.SZ', '601059.SH', '300114.SZ', '002792.SZ', '002354.SZ']}, {'20230207': ['600817.SH', '002855.SZ', '002813.SZ', '002362.SZ', '601059.SH', '300114.SZ', '002354.SZ']}, {'20230206': ['002226.SZ', '002347.SZ', '600817.SH', '002855.SZ', '002813.SZ', '002362.SZ', '002512.SZ', '601059.SH', '600212.SH', '002574.SZ', '300114.SZ', '002354.SZ']}, {'20230203': ['002347.SZ', '002362.SZ', '601059.SH', '002835.SZ', '300114.SZ']}, {'20230202': ['002713.SZ', '002877.SZ', '002362.SZ', '002209.SZ', '603281.SH', '601059.SH', '002835.SZ', '300114.SZ', '002122.SZ', '002167.SZ']}, {'20230201': ['002877.SZ', '002362.SZ', '002209.SZ', '603281.SH', '002835.SZ', '002708.SZ', '002122.SZ', '600136.SH', '600819.SH', '002167.SZ']}, {'20230131': ['603007.SH', '003011.SZ', '605133.SH', '603173.SH', '002253.SZ', '002362.SZ', '002835.SZ', '002708.SZ', '603929.SH']}, {'20230130': ['003007.SZ', '688787.SH', '600358.SH', '605133.SH', '688327.SH', '000796.SZ', '002362.SZ', '300229.SZ', '002209.SZ', '002835.SZ', '002380.SZ', '002808.SZ']}, {'20230120': ['600358.SH', '002178.SZ', '002209.SZ', '002380.SZ', '002808.SZ']}, {'20230119': ['002725.SZ', '002334.SZ', '002309.SZ', '002209.SZ', '603703.SH', '600611.SH', '601699.SH', '002808.SZ']}, {'20230118': ['002725.SZ', '002086.SZ', '002334.SZ', '000026.SZ', '601828.SH', '002927.SZ', '002808.SZ', '002686.SZ']}, {'20230117': ['000417.SZ', '002144.SZ', '601828.SH', '002808.SZ']}, {'20230116': ['000564.SZ', '601828.SH', '002927.SZ', '000701.SZ', '002560.SZ']}, {'20230113': ['600658.SH', '600589.SH', '002927.SZ', '600136.SH', '002560.SZ', '002616.SZ']}, {'20230112': ['600658.SH', '000026.SZ', '600136.SH', '002560.SZ', '603028.SH']}, {'20230111': ['600658.SH', '002103.SZ', '002669.SZ', '002576.SZ', '603595.SH', '002717.SZ']}, {'20230110': ['600658.SH', '600038.SH', '603595.SH', '002717.SZ', '002482.SZ', '001298.SZ', '600136.SH']}, {'20230109': ['600658.SH', '002083.SZ', '002576.SZ', '002482.SZ', '002433.SZ', '600136.SH', '000637.SZ', '002195.SZ']}, {'20230106': ['002043.SZ', '300389.SZ', '603390.SH', '002576.SZ', '600734.SH', '600136.SH']}, {'20230105': ['002696.SZ', '002235.SZ', '600734.SH', '002348.SZ', '002184.SZ', '002615.SZ', '600136.SH']}, {'20230104': ['603912.SH', '603825.SH', '600599.SH', '002235.SZ', '000045.SZ', '600734.SH', '002231.SZ', '000948.SZ', '002615.SZ', '002988.SZ', '600136.SH', '000938.SZ', '002279.SZ', '001301.SZ']}, {'20230103': ['600785.SH', '603998.SH', '300086.SZ', '600599.SH', '002235.SZ', '000045.SZ', '002826.SZ', '000972.SZ', '000419.SZ', '001301.SZ']}, {'20221230': ['002022.SZ', '600303.SH', '603856.SH', '000419.SZ', '000715.SZ', '001301.SZ']}, {'20221229': ['600187.SH', '002614.SZ', '002022.SZ', '600593.SH', '002235.SZ', '002213.SZ', '001301.SZ']}, {'20221228': ['600187.SH', '601136.SH', '000620.SZ', '600853.SH', '603255.SH']}, {'20221227': ['600187.SH', '002062.SZ', '601136.SH', '002095.SZ', '002719.SZ', '002159.SZ', '002933.SZ', '603255.SH']}, {'20221226': ['002086.SZ', '601136.SH', '600601.SH', '000810.SZ', '600816.SH', '002933.SZ']}, {'20221223': ['002422.SZ', '601136.SH', '002076.SZ', '600601.SH', '002516.SZ', '002574.SZ', '002933.SZ']}, {'20221222': ['002864.SZ', '002582.SZ', '002076.SZ', '600599.SH', '002186.SZ', '002933.SZ', '600729.SH']}, {'20221221': ['002623.SZ', '600241.SH', '002076.SZ', '600599.SH']}, {'20221220': ['603912.SH', '300049.SZ', '002095.SZ', '301169.SZ']}, {'20221219': ['002793.SZ', '002095.SZ', '600684.SH', '000597.SZ', '002259.SZ', '600056.SH', '002172.SZ', '600185.SH', '002162.SZ']}, {'20221216': ['600671.SH', '000679.SZ', '600056.SH', '600663.SH', '600185.SH']}, {'20221215': ['000679.SZ', '000721.SZ', '002259.SZ', '600056.SH', '600185.SH', '600238.SH']}, {'20221214': ['002316.SZ', '002269.SZ', '003026.SZ', '000721.SZ', '002898.SZ', '002259.SZ', '600185.SH', '002357.SZ']}, {'20221213': ['000756.SZ', '002259.SZ', '600185.SH', '002316.SZ', '601022.SH']}, {'20221212': ['002362.SZ', '002420.SZ', '002336.SZ', '002259.SZ', '600185.SH', '603603.SH', '603387.SH', '601022.SH', '600239.SH']}, {'20221209': ['601022.SH', '601226.SH', '000796.SZ', '600599.SH', '002742.SZ', '002206.SZ', '002336.SZ', '002315.SZ', '600301.SH', '600185.SH', '300858.SZ', '001256.SZ']}, {'20221208': ['000705.SZ', '000796.SZ', '600599.SH', '000564.SZ', '002336.SZ', '688247.SH', '001256.SZ']}, {'20221207': ['600693.SH', '002427.SZ', '600599.SH', '002742.SZ', '601116.SH', '002433.SZ', '688247.SH', '600415.SH', '002776.SZ', '000752.SZ', '001256.SZ']}, {'20221206': ['600303.SH', '600225.SH', '002427.SZ', '600599.SH', '000958.SZ', '603000.SH', '002742.SZ', '002433.SZ', '002776.SZ', '000752.SZ', '001256.SZ']}, {'20221205': ['002462.SZ', '002424.SZ', '002052.SZ', '000608.SZ', '002076.SZ', '002732.SZ', '002427.SZ', '002235.SZ', '603000.SH', '002528.SZ', '002742.SZ', '001338.SZ', '600493.SH', '002599.SZ', '002776.SZ', '002435.SZ']}, {'20221202': ['001318.SZ', '002052.SZ', '002732.SZ', '002427.SZ', '001338.SZ', '002599.SZ', '000006.SZ', '002150.SZ']}, {'20221201': ['002776.SZ', '000800.SZ', '001338.SZ', '600332.SH', '002187.SZ', '002427.SZ', '002420.SZ', '000796.SZ', '600518.SH', '000736.SZ', '000797.SZ', '600675.SH', '000888.SZ', '600094.SH', '000006.SZ', '002561.SZ', '002923.SZ', '002150.SZ']}, {'20221130': ['000564.SZ', '002420.SZ', '600823.SH', '600791.SH', '600622.SH', '600112.SH', '600266.SH', '000926.SZ', '000736.SZ', '000797.SZ', '601858.SH', '600675.SH', '002305.SZ', '600159.SH', '002089.SZ', '000888.SZ', '002382.SZ', '600657.SH', '002150.SZ', '002398.SZ']}, {'20221129': ['000514.SZ', '000564.SZ', '600791.SH', '002016.SZ', '600622.SH', '002875.SZ', '600266.SH', '002789.SZ', '000736.SZ', '000797.SZ', '601858.SH', '603506.SH', '000608.SZ', '600675.SH', '002305.SZ', '000014.SZ', '600463.SH', '002314.SZ', '002089.SZ', '600173.SH', '000006.SZ', '600322.SH', '002316.SZ', '600657.SH', '000632.SZ', '002150.SZ', '600239.SH']}, {'20221128': ['002776.SZ', '000564.SZ', '002875.SZ', '000797.SZ', '601858.SH', '600601.SH', '002316.SZ', '002150.SZ']}, {'20221125': ['002776.SZ', '002875.SZ', '000797.SZ', '002316.SZ', '002150.SZ', '002795.SZ']}, {'20221124': ['001338.SZ', '002564.SZ', '002875.SZ', '002076.SZ', '002348.SZ', '000151.SZ', '601858.SH', '600601.SH', '002116.SZ', '002150.SZ', '002795.SZ']}, {'20221123': ['001338.SZ', '000045.SZ', '000971.SZ', '002348.SZ', '000151.SZ', '002150.SZ']}, {'20221122': ['000564.SZ', '001338.SZ', '000971.SZ', '002875.SZ', '002846.SZ', '002348.SZ', '603130.SH', '600222.SH']}, {'20221121': ['001338.SZ', '002551.SZ', '002072.SZ', '600222.SH']}]
# for i in dict:
#     print(i)
#     for key, value in i.items():
#         xtdata.download_history_data2(stock_list=value, period='tick', start_time=key, end_time=key, callback=on_progress)
#         time.sleep(2)