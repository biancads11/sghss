from rest_framework import response
from rest_framework import serializers
from rest_framework.decorators import action


class HistoryViewSetMixin:
    """
    Mixin que adiciona uma action '/history/' para qualquer ViewSet.
    """

    @action(detail=True, methods=['get'], url_path='history')
    def get_history(self, request, pk=None):
        """
        Retorna o histórico de alterações para um objeto específico.
        """
        obj = self.get_object()

        # Verifica se o modelo realmente tem um histórico
        if not hasattr(obj, 'history'):
            return response.Response(
                {"error": "Este objeto não possui histórico de alterações."},
                status=404
            )

        # Cria um serializer genérico para o histórico
        class HistoricalSerializer(serializers.ModelSerializer):
            history_user_name = serializers.CharField(source='history_user.name', read_only=True, default=None)

            class Meta:
                model = obj.history.model
                fields = '__all__'

        history = obj.history.all()
        serializer = HistoricalSerializer(history, many=True)
        return response.Response(serializer.data)
