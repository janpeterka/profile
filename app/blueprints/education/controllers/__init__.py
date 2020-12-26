from .genetic_world_generator import WorldView

__all__ = [
    "WorldView",
]


def register_all_controllers(application):
    WorldView.register(application)