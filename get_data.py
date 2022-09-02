from eth_log.models.contract import Contract
from web3 import Web3
from web3.auto import w3
import eth_event
import json
from hexbytes import HexBytes
from ast import literal_eval
from attributedict.collections import AttributeDict
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
        return
def change_glob(x,v):
    globals()[x] = v
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def in_it(x,y):
    if str(x) in y:
        return True
    return False
def get_txn_data(x,LP):
    h = read_hex(x.transactionHash)
    a = x.contract
    try:
        expo = float(get_expo(str(a).lower()))
    except:
        expo = float(str('1e-18'))
    try:
        d = get_hex_data(x.data)*expo
    except:
        return False
    return h,a,d
def mains(x):
    from web3 import Web3
    global net,ch_id,main,file,w3,last_api,c_k,hashs_js,expo,dec
    hashs_js = ''
    last_api = [0,0]
    scan = ['avax','polygon','ethereum','cronos_test','optimism','binance']
    main = {
        'avax':{'net':'https://api.avax.network/ext/bc/C/rpc','chain':'43114','main':'AVAX'},
            'polygon':{'net':'https://polygon-rpc.com/','chain':'137','main':'MATIC'},
            'ethereum':{'net':'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161','chain':'1','main':'ETH'},
            'cronos_test':{'net':'https://cronos-testnet-3.crypto.org:8545/','chain':'338','main':'TCRO'},
            'optimism':{'net':'https://kovan.optimism.io','chain':'69','main':'OPT'},
            'binance':{'net':'https://bsc-dataseed.binance.org/','chain':'56','main':'bsc'}
            }
    expo = ''
    dec = ''
    main = main[x]
    net,ch_id,main,file,w3 = main['net'],main['chain'],main['main'],str(x)+'.txt',Web3(Web3.HTTPProvider(main['net']))
    c_k = 0
    return net,ch_id,main,file,w3
def check_sum(x):
    return Web3.toChecksumAddress(str(x))
def read_hex(hb):
    h = "".join(["{:02X}".format(b) for b in hb])
    return '0x'+h
def get_hex_data(x):
    n = len(x)
    hex = x
    return int(hex, n)
def get_expo(x):
    n = '1e-'+str(get_dec(x))
    return float(n)
def in_it(x,y):
    if str(x) in y:
        return True
    return False
def find_it(x,y):
    if in_it(x,y) == True:
        for i in range(0,len(y)):
            if str(x) == str(y[i]):
                return i
    return False
##def get_hex_data(x):
    hex = x
    return int(hex, 16)
def get_txn_stuff(x):
    h = read_hex(x.transactionHash)
    l = str(head_hex(h))
    a = x.address
    t = x.topics
    d = x.data
    return h,l,a,t,d
def get_txn_data(x):
    string = read_hex(x)
    de = literal_eval(string)
    return de
def find_it(x,y):
    if in_it(x,y) == True:
        for i in range(0,len(y)):
            if str(x) == str(y[i]):
                return i
    return False
def get_c(i):
    c = ''
    if i != 0:
        c = ',\n'
    return c
def js_wrap_it(x,y,i):
    c = get_c(i)
    return str(c)+'"'+str(x)+'":'+str(y)+''
def try_it_js(x,js):
    try:
        n = js[x]
        return True
    except:
        return False
def head_hex(x):
    h = '0x'
    if h in str(x):
        x = str(x)[2:]
    else:
        x = read_hex(str(h+str(x)))
    return x
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def timer(i):
    return int(int(i)+ int(1))
def hash_update(x,y):
    x = js_it('{'+str(x)[1:-1]+js_wrap_it(str(y),'{}',len(x))+'}')
    x["hash_pairs"] = js_it('{'+str(x["hash_pairs"])[1:-1] +js_wrap_it(str(y),'[],"txns":[]',len(x["hash_pairs"]))+'}')
    x["hashs"].append(str(y))
    x = js_it(x)
    change_glob('hashs_js',x)
    return x
def add_update(x,y,z):
    x = js_it(x)
    x[str(y)] = js_it(str(x[str(y)])[-1] +js_wrap_it(str(z),'{"amt":[],"event":[]}',len(x[str(y)]))+'}')
    x["hash_pairs"][str(y)].append(str(z))
    change_glob('hashs_js',x)
    return x
def js_it(x):
    return json.loads(str(x).replace("'",'"'))
def kek(x):
    st = '"'+str(x)+'"'
    return w3.keccak(text=str(x)).hex()
def c_res():
    change_glob('c_k',int(0))
def c_cou(c_k):
    c_k = timer(c_k)
    change_glob('c_k',int(c_k))
def for_it(x):
    if int(c_k) <= len(x):
        x = c_cou(c_k)
        return True
    else:
        x = c_res()
        return False
def get_events(x):
    x = w3.eth.getFilterLogs(x.filter_id)
    return x
def exists(x):
    try:
        x = reader(x)
        return x
    except:
        return ''
def get_expo(x):
    expo = str('1e')+str('-'+str(x))
    expo = float(str(expo))
    change_glob('expo',expo)
    return expo
def get_dec():
    dec = cont.functions.decimals().call()
    change_glob('dec',str(dec))
    expo = get_expo(dec)
    return dec,expo
def get_abi(x):
    x = js_it(reader(x))
    change_glob('abi',x)
def get_cont(x,y):
    #get_abi(y)
    cont = w3.eth.contract(x,abi = y)
    change_glob('cont',cont)
    return cont
def save_events(x,y):
    c = ''
    if len(x) > 0:
        c = ','
    x = str(exists(y))[:-1]+c+str(x)


    pen(x,y)
def join_it(x,y):
    return str(x)+str(y)
def txt_it(x):
    return str(x) +'.txt'
def js_qu(x):
    if type(x) is not list:
        return '"'+str(x)+'"'
    ls = []
    for i in range(0,len(x)):
        ls.append('"'+str(x[i])+'"')
    return x
def add_js(x,y):
    print(str(x)[:-1] + get_c(len(x)) + str(y)+str(x)[-1])
    return js_it(str(x)[:-1] + get_c(len(x)) + str(y)+str(x)[-1])
def get_vars(x):
    y = str(x)
    v_1,v_2 = [],[]
    if ':' in y:
        n = str(x)[1:-1].split(',')
        for i in range(0,len(n)):
            v = str(n[i]).replace('"','').replace("'",'').replace(' ','').split(':')
            v_1.append(v[0])
            v_2.append(v[1])
    return v_1,v_2
def gen_fun(x,y):
    n = ['indexed', 'internalType', 'name', 'type']
    y = y['name']+'('+y['type']+')'
    print(y)
    return y
net,ch_id,main,file,w3=mains('binance')
pairs = check_sum('0xd8cab604bdd8cbb7c3eb0c26f7dc3abffb005a92')

abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
cont = get_cont(pairs,abi)
lm = w3.eth.getStorageAt(pairs, '0x89ec16a653c3965e8ec37d73b0de51b6df7167dc0390ac11460edae0fd33bd61')
print(read_hex(w3.eth.getStorageAt(pairs, '0x89ec16a653c3965e8ec37d73b0de51b6df7167dc0390ac11460edae0fd33bd61')))
print(read_hex(lm))
print(kek('Permit(address owner,address spender,uint256 value,uint256 nonce,uint256 deadline)'))
print(kek('EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)'))
print(kek('mint(address 0x7d083f61F114fF2582d73b1dd6843FAeFA88ADeF)'))
print(kek('initializeV1(address _authKey)'))
print(kek('eip1967.proxy.implementation'))
