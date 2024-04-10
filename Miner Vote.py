import msvcrt
try:
    from TonTools import *
    import asyncio, time, json

    with open("config.json", "r") as file:
        config_data = json.load(file)

    giver = config_data["giver"]
    mnemonics = config_data["SEED"]

    if giver == "small":
        address = "EQDl1Rk1Lz8MwpUsTgKjhMWX3ad2F0R4UDnjsl4-z3ExZZq7"
    elif giver == "extra_small":
        adress = "EQD6dEF4pPrbyz4SeQOkiXUcelcR72rstlZv_2CY6-YyCKR7"
    elif giver == "medium":
        address = "EQDrtlyVn7Q_1pheIgyJZn0neMyG5TizQ3b6lCP89B6LuePY"
    else:
        print("Giver not found, use: extra_small, small, medium")
        print("Press button to exit")
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key:
                    exit()

    n = 0

    async def main():
        global n, tons
        client = TonCenterClient(orbs_access=True)
        wallet = Wallet(provider=client, mnemonics=mnemonics, version='v4r2')
        print("Use wallet:", wallet.address)
        print("  [time]      [counts]       [balance]")
        while True:
            balance = await wallet.get_balance() / 1000000000
            if balance < 0.00:
                print("balance less than 0.05, retry after 30 sec")
                await asyncio.sleep(30)
                pass
            else:
                await wallet.transfer_ton(amount=0.05, destination_address=address)
                current_time = time.strftime("%H:%M:%S")
                n += 1
                print(f"[{current_time}]       {int(n)}          {balance}")
                await asyncio.sleep(3)


    if __name__ == '__main__':
        asyncio.run(main())

except Exception as e:
        print(f"Error: {e}")
        print("Press button to exit")
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key:
                    exit()