import parse
import asyncio
import json_formatter as jf


asyncio.run(parse.parse_channel())
parsed_json = parse.parse_json()

print(jf.get_message(parsed_json))
