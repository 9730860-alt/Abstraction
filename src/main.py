from abc import ABC, abstractmethod


class CookingPlan(ABC):

    def __init__(self, dish_name: str):
        if not dish_name or not dish_name.strip():
            raise ValueError("Dish name cannot be empty or whitespace-only.")
        self._dish_name: str = dish_name.strip()

    def get_dish_name(self) -> str:
        return self._dish_name

    @abstractmethod
    def cook(self) -> list[str]:
        pass


class OvenPlan(CookingPlan):

    def cook(self) -> list[str]:
        return [
            "Prepare the oven and baking dish.",
            f"Place {self.get_dish_name()} in the baking dish.",
            "Bake using the recipe's oven instructions.",
        ]


class StovetopPlan(CookingPlan):

    def cook(self) -> list[str]:
        return [
            "Prepare the stovetop and pan.",
            f"Place {self.get_dish_name()} in the pan.",
            "Cook using the recipe's stovetop instructions.",
        ]


class CampingPlan(CookingPlan):

    def cook(self) -> list[str]:
        return [
            "Prepare the portable stove and camping pot.",
            f"Place {self.get_dish_name()} in the camping pot.",
            "Cook using the recipe's portable-stove instructions.",
        ]


class RecipeApp:

    @staticmethod
    def show_plan(plan: CookingPlan) -> None:
        print(f"--- {plan.get_dish_name()} ---")
        for instruction in plan.cook():
            print(f"- {instruction}")
        print()

    @classmethod
    def main(cls) -> None:
        plans: list[CookingPlan] = [
            OvenPlan("Demo Dish"),
            StovetopPlan("Demo Dish"),
            CampingPlan("Demo Dish"),
            CampingPlan("Trail Meal"),
        ]

        for plan in plans:
            cls.show_plan(plan)


if __name__ == "__main__":
    RecipeApp.main()
