extends Node2D

var http_request = HTTPRequest.new()
func _ready():
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	http_request.request("http://127.0.0.1:5000/get_posicao")


func _http_request_completed(result, response_code, headers, body):
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	print(response) # id, x, y, rotacao

	await get_tree().create_timer(0.5).timeout
	print(response)
	$Robozinho.position.x = response['posicao_x']
	$Robozinho.position.y = response['posicao_y']
	$Robozinho.rotation = response['rotacao']
	$Timer.start()


func _on_timer_timeout():
	http_request.request("http://127.0.0.1:5000/get_posicao")
