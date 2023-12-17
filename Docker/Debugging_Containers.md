Having issues with containers? Here are some handy tips when debugging some work!

# Step 1: Is your container even running mate?

`docker container ls --all`

Gives you some extra info regarding containers

You wanna see a bit more information regarding your container but the naughty terminal is cutting of the information you need (very rude isn't it?). Format the output of the above command mate

`docker container ls --all --format ‘{{ json . }}’ | python3 -m json.tool --json-lines`

# Step 2: So its running, that's nice. Can you go inside and have a little looksy? maybe something weird got inside

`docker run --rm --it --name MYCONTAINER [IMAGE] bash`

`--rm` removes container when finished
`--i` interactive terminal in container. Have a little play around 
`--name` name of container