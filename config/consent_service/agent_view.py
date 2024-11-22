from rest_framework.viewsets import ModelViewSet
from .agent_model import Agent, AgentSerializer


class AgentViewSet(ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
