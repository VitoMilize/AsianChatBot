import requests


def send_request(api_key="AQVN0QEJkNFJedapfxBdj50JfwzDGdNwPS-hpncx", folder_id="b1g03bof94p6rf6cc0oi"):
    resp = requests.post(
        url="https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
        headers={
            "Authorization": f"API-KEY {api_key}",
            "x-folder-id": folder_id
        },
        json={
            "modelUri": f"gpt://{folder_id}/yandexgpt/latest",
            "completionOptions": {
                "stream": False,
                "temperature": 0.1,
                "maxTokens": "1000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": "Переведи текст на русский"
                },
                {
                    "role": "user",
                    "text": "2016年12月16日から18日の日程で、韓国ギョンギ道のギョンギジムにおいて開催された、世界最大規模のeスポーツ世界大会「Intel Extreme Masters（IEM）」ギョンギ大会。最終日の18日に、今回の大会で競われた3タイトルの決勝戦が行われた。\n今回のIEMギョンギ大会で競われた種目は「Overwatch」、「StarCraft II」、そして「League of Legends」の3タイトル。 こちらの記事 で紹介しているように、16日と17日にそれぞれの種目でトーナメント戦を開催して決勝進出2チームを選出。そして、最終日の18日に全種目の決勝戦が行われた。\nまず最初に決勝戦が行われたのが、Overwatchだ。6人対6人のチーム戦で、最大5戦の3戦先勝マッチで競った。決勝に進出したのは、チーム「Lunatic Hai」と、チーム「Luxury Watch Red」。どちらも準々決勝を3勝0敗、準決勝を3勝1敗と、圧倒的な強さで勝ち上がってきたチームで、決勝戦は実力伯仲。実際、決勝戦の最初の2戦は、双方が1勝ずつと、期待通りの立ち上がりとなった。"
                }
            ]
        }
    )

    answer = resp.json()
    text_answer = answer['result']['alternatives'][0]['message']['text']
    print(text_answer)
    return text_answer
