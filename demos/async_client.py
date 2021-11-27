import asyncio

import invaultapi
import invaultapi.message as message


url = "http://localhost:8084/open/api/v1"
private_key = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC960PRWoig87lgEhVRPSCd8wNFxT3FHs8DrT9mRjyb0bTlZHOqpR846AZfWlLJn2pbFQCILPlHnKY51HHoMPd0VuaZrBRa62rmVhrlNRsMYV/RsZZWaYloUcnDMyvqDP2Xg6CI4dNXSwl8vJDLzJHiwD+ZWE/AxjZftA0QqdQyuaRxwoabbZiYHtFxynN14KoEhhp6ElWd3S+b/4O7pg99BfqOnZtXNEJiUgLdDjrqGr6HgxZP7djPhQFgx9m4vVvNIfjUxGS35UcvrNJTT/QrLguQ84g+UHi1/Yz7W/G9yyPKvVuTmH3v+i3JBEt/Yk9H/o9J8k8tOLxOOvc4PFufAgMBAAECggEAHiWRP1MyqvHlNCXKsnmUit3/X/zeQEMSs0+156Mwjb9tCpi2b5kEasER+eLZj125wTmFOxiAfWiVTkq1xhi3vwToV+5j0Mbb0jJK1KVoZL+0ORIKfi8Ee8W31D90MhPb0Ug4nGHUbV/g4qcACQmxAqBnuAy3pC8ShICNLl726xIczUsn1MKbzavZNEAejYYs9YMaxyNwg3Qiw9SgCpM3UG85VIV6XuMnj1NypX6pGDv9bu3Sd4SI+OmfaG4GtgsDLE4aP7UMC848qnUnOASOkMmJRcfNWzceFkYCotJ6EUu3GraYdqTRzkz7HCkMCxTYhcanEFWKy/ZLn9VtiheJkQKBgQDiAnE6sxyyKNDJxgI53ELrBx80HgAJy3JcA/u3KN6xkMg0k6iji9X6XP0XDGBLSrnDJcpiJUxiYuVXyhntFS8D2FYIkcNuaPgS5aqzvmBm5PFpqRrCtZiOWqW/t1udGUt3RRt7lyjyUGLfh2oJHHpjjjfqymUB9xLUH+rfRrBtCQKBgQDXHtMtDP8DtjW4VNuSa45g64jmv1YAjD47HydpE76VnrZC5fI259oMzSzopGCA/H6YCkHinl0KHLsE3APNx0T7ID+CkAuGcVJuX0Y38t8AL8RYfciAjn1damBRig7tEmeY38FYN12YSzCa7qTo4gKuBHUxbiOUyNxDuHZmQkjVZwKBgQDU4XwJ0F/9KBjRlWLPYTre6gxoKMHcd/c12MKmGSb5legeLd8wfSyF8ESsCwpAoRgsSlJA8+To30Iq2MBm4gcw1frjg3jTbKgOFKofN/jRsl/6KEB+mlIh9BwfYvQ2G3dL1po2ZYE6DKG07nXgMyTM1U6yJwXRPgpMJ+wxdwIDEQKBgFhxE+ExtqaQAwYF3UAVeDPgoig8Ad+3yN4FsO5Cb9iTp9tZLnvkVoFs2UnMSuC87k8T6IKDGT1PEpSs3+N6SaH1YCcNka90Z694/CWEdKpe+RponEY+TsxZL8BWQky1hGIVnCfom1JBl3obIzGbuf5RVt07quVAr04oSIVCOy+BAoGARAUBCrjprBhn53OkWt6YjmUqMyT4cgIeo+zIjr/n7+TRrcvpFK6/MabSLlJ5AHsU1N95mXjrBv2IIM9TgybtNkK228IOjs5aBZiIDc3DMkHN6tneO+61QaM9oBPW/MR3bgL3X5uai8fy14nNVFOJA7eTriQ1ENTtybxhNyeDh7I="
keyid = "83c846b2433348da837b3aeb2e76fea6"
client = invaultapi.AsyncClient(url, private_key, keyid)

if "__main__" == __name__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete

    # assets.xxx api
    try:
        params = message.QueryAddressesByCoinCodeParams(coinCode = "ETH", pageNum = 0)
        resp = loop.run_until_complete(client.assets.query_addresses_by_coin_code(params))
        print("query_addresses_by_coin_code", resp)
    except RuntimeError as e:
        print(e.args[0])
        raise
    except Exception as e:
        print(e)
        raise

    # transaction.xxx api
    try:
        params = message.BlockHeightParams(chainCoin = "BTC")
        resp = loop.run_until_complete(client.transaction.block_height(params))
        print("block_height", resp)
    except RuntimeError as e:
        print(e.args[0])
        raise
    except Exception as e:
        print(e)
        raise

    # withdraw.xxx api
    try:
        params = message.WithdrawApplyParams(coinCode = "BTC")
        resp = loop.run_until_complete(client.withdraw.withdraw_apply(params))
        print("withdraw_apply", resp)
    except RuntimeError as e:
        print(e.args[0])
        raise
    except Exception as e:
        print(e)
        raise
