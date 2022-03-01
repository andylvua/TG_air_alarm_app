def get_message(parsed_json):
    for i in range(len(parsed_json)-1):
        if parsed_json[i]["_"] == "Message":
            message = parsed_json[i]["message"]
            return str(i+1) + " Message: " + str(message)
