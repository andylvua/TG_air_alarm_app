def get_last_message(parsed_json):
    for i in range(len(parsed_json)):
        if parsed_json[i]["_"] == "Message":
            message = parsed_json[i]["message"]
            print(str(i+1) + " last message: " + str(message))
