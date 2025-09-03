from flask import Blueprint, jsonify, request
from controllers.tarefa_controller import TarefaController

tarefas_bp = Blueprint('tarefas', __name__)


@tarefas_bp.route('/api/tarefas', methods=['GET'])
def get_listar_tarefas():
    return jsonify([tarefa.to_dict() for tarefa in TarefaController.get_listar_tarefas()])


@tarefas_bp.route('/api/tarefas/<int:tarefa_id>', methods=['POST'])
def criar_tarefa(tarefa_id):
    dados = request.get_json()
    id = dados.get('id')
    titulo = dados.get('titulo')
    concluida = dados.get('concluida') 
    nova_tarefa = TarefaController.criar_tarefa(id, titulo, concluida)
    return jsonify(nova_tarefa.to_dict()), 201 