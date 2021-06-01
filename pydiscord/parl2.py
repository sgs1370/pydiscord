import requests

url = "https://api.opensea.io/api/v1/events"

import time
now = time.time()
twoday = now - 57200.0

#querystring = {"only_opensea":"false","offset":"0","limit":"20","collection_slug":"veefriends","occurred_after":twoday,"event_type":"successful"}
querystring = {"only_opensea":"false","offset":"0","limit":"20","collection_slug":"veefriends","occurred_after":twoday,"event_type":"successful"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)
#print(dir(response))

import json
json_data = json.loads(response.text)

out = json.dumps(json_data,indent=2)

events = json_data["asset_events"]

for event in events:
    asset = event["asset"]
    print(asset["image_url"],asset["name"],(int(event["total_price"])/2400000000000000000.0),event["winner_account"])
    print('+++++++++++++')

"""

{
  "asset_events": [
    {
      "approved_account": null,
      "asset": {
        "id": 25986219,
        "token_id": "17773364155682651268275142113690502555604463656341524695465728159671423860737",
        "num_sales": 1,
        "background_color": null,
        "image_url": "https://lh3.googleusercontent.com/5XZ1eWNjc4tARteFGhkncrz5OSCc1SdpHoTbRmCi9e6IY9EBrvLFqQDUp8t_VDeJtQYFGNo-LTpUv8cfF2DXdIUn-01FVA9Euf6WQg",
        "image_preview_url": "https://lh3.googleusercontent.com/5XZ1eWNjc4tARteFGhkncrz5OSCc1SdpHoTbRmCi9e6IY9EBrvLFqQDUp8t_VDeJtQYFGNo-LTpUv8cfF2DXdIUn-01FVA9Euf6WQg=s250",
        "image_thumbnail_url": "https://lh3.googleusercontent.com/5XZ1eWNjc4tARteFGhkncrz5OSCc1SdpHoTbRmCi9e6IY9EBrvLFqQDUp8t_VDeJtQYFGNo-LTpUv8cfF2DXdIUn-01FVA9Euf6WQg=s128",
        "image_original_url": null,
        "animation_url": null,
        "animation_original_url": null,
        "name": "BitShield #62",
        "description": "Mustard",
        "external_link": null,
        "asset_contract": {
          "address": "0x495f947276749ce646f68ac8c248420045cb7b5e",
          "asset_contract_type": "semi-fungible",
          "created_date": "2020-12-02T17:40:53.232025",
          "name": "OpenSea Collection",
          "nft_version": null,
          "opensea_version": "2.0.0",
          "owner": 102384,
          "schema_name": "ERC1155",
          "symbol": "OPENSTORE",
          "total_supply": null,
          "description": null,
          "external_link": null,
          "image_url": null,
          "default_to_fiat": false,
          "dev_buyer_fee_basis_points": 0,
          "dev_seller_fee_basis_points": 0,
          "only_proxied_transfers": false,
          "opensea_buyer_fee_basis_points": 0,
          "opensea_seller_fee_basis_points": 250,
          "buyer_fee_basis_points": 0,
          "seller_fee_basis_points": 250,
          "payout_address": null
        },
        "permalink": "https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/17773364155682651268275142113690502555604463656341524695465728159671423860737",
        "collection": {
          "banner_image_url": null,
          "chat_url": null,
          "created_date": "2021-05-09T22:53:50.969472",
          "default_to_fiat": false,
          "description": "BitShields is a collection of different pixelated shields! \n\nAll shields are 1/1.\n\nThere are some \"Sets\" of shields... these shields have the same design, but a 5 different color variations!\n\nVisit our twitter for updates on drops / giveaways: https://twitter.com/BitShields_NFT\n\nPrice Floor:\n#1-100: 0.02 ETH\n#101-200: ?\n#201-300: ?\n#301-400: ?\n#401-500: ?\n#501-600: ?\n#601-700: ?\n#701-800: ?\n#801-900: ?\n#901-1000: ?",
          "dev_buyer_fee_basis_points": "0",
          "dev_seller_fee_basis_points": "1000",
          "discord_url": null,
          "display_data": {
            "card_display_style": "contain"
          },
          "external_url": null,
          "featured": false,
          "featured_image_url": null,
          "hidden": true,
          "safelist_request_status": "not_requested",
          "image_url": "https://lh3.googleusercontent.com/a-yjHhT464YOuaZnmrlcZNkWYLXWmrkZBYLuf44J779koUDTA0bnCXLspmut6Z98WgTlax8c5iexPXQYh5dRIm4xbOeR7myOH7Qecw=s120",
          "is_subject_to_whitelist": false,
          "large_image_url": null,
          "medium_username": null,
          "name": "BitShields",
          "only_proxied_transfers": false,
          "opensea_buyer_fee_basis_points": "0",
          "opensea_seller_fee_basis_points": "250",
          "payout_address": "0x274b5e1c7257f1092402c2d2ffb987010a48496d",
          "require_email": false,
          "short_description": null,
          "slug": "bitshields",
          "telegram_url": null,
          "twitter_username": "BitShields_NFT",
          "instagram_username": null,
          "wiki_url": null
        },
        "decimals": null,
        "token_metadata": null,
        "owner": {
          "user": {
            "username": "NullAddress"
          },
          "profile_img_url": "https://storage.googleapis.com/opensea-static/opensea-profile/1.png",
          "address": "0x0000000000000000000000000000000000000000",
          "config": "",
          "discord_id": ""
        }
      },
      "asset_bundle": null,
      "auction_type": null,
      "bid_amount": null,
      "collection_slug": "bitshields",
      "contract_address": "0x495f947276749ce646f68ac8c248420045cb7b5e",
      "created_date": "2021-06-01T15:29:44.712663",
      "custom_event_name": null,
      "dev_fee_payment_event": null,
      "duration": null,
      "ending_price": null,
      "event_type": "transfer",
      "from_account": {
        "user": {
          "username": "Corso5"
        },
        "profile_img_url": "https://storage.googleapis.com/opensea-static/opensea-profile/20.png",
        "address": "0x274b5e1c7257f1092402c2d2ffb987010a48496d",
        "config": "",
        "discord_id": ""
      },
      "id": 185760441,
      "owner_account": null,
      "payment_token": null,
      "quantity": "1",
      "seller": null,
      "starting_price": null,
      "to_account": {
        "user": {
          "username": "girlmomholly"
        },
        "profile_img_url": "https://storage.googleapis.com/opensea-static/opensea-profile/10.png",
        "address": "0xbaaabce9d8b6e0e7b26e107f33ddfc7bd582e301",
        "config": "",
        "discord_id": ""
      },
      "total_price": null,
      "transaction": {
        "block_hash": "0xc226327ca75604b1a41fffb98f538ac34f53bce07b613921975b36fdf867cf23",
        "block_number": "12549372",
        "from_account": {
          "user": {
            "username": "girlmomholly"
          },
          "profile_img_url": "https://storage.googleapis.com/opensea-static/opensea-profile/10.png",
          "address": "0xbaaabce9d8b6e0e7b26e107f33ddfc7bd582e301",
          "config": "",
          "discord_id": ""
        },
        "id": 121105943,
        "timestamp": "2021-06-01T15:27:32",
        "to_account": {
          "user": {
            "username": "OpenSea-Orders"
          },
          "profile_img_url": "https://storage.googleapis.com/opensea-static/opensea-profile/22.png",
          "address": "0x7be8076f4ea4a4ad08075c2508e481d6c946d12b",
          "config": "verified",
          "discord_id": ""
        },
        "transaction_hash": "0x95f20924ad771c0b097ab5ac623e87f058f3ebe63ed273c17cd0a35d452a4b1c",
        "transaction_index": "190"
      },
      "winner_account": null
    }
  ]
}

"""
