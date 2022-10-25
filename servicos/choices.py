from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCA_VALVULA_MOTOR = "TVM","Trocar valvula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO = "B", "Balanceamento"
    ALINHAMENTO = "AL", "Alinhamento"
    