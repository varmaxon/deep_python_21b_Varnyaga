from random import uniform


class SomeModel:
    def predict(self, message: str) -> float:
        return uniform(0, 1) * len(message)


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if isinstance(message, str) and isinstance(model, SomeModel):
        y_predict = model.predict(message)
        if y_predict < bad_thresholds:
            return "неуд"

        if y_predict > good_thresholds:
            return "отл"

        return "норм"

    raise TypeError('input correct type of params')


# new_model = SomeModel()
# assert predict_message_mood("Чапаев и пустота", new_model) == "отл"
# assert predict_message_mood("Вулкан", new_model) == "неуд"
