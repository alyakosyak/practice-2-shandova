from plt_temp import create_dataframe


def test_create_dataframe():
    hours = [
        "2026-01-01T03:00",
        "2026-01-01T01:00",
        "2026-01-01T02:00",
    ]

    temperatures = [3.0, 1.0, 2.0]

    df = create_dataframe(hours, temperatures)

    # Проверяем названия столбцов
    assert list(df.columns) == ["time", "temperature_c"]

    # Проверяем количество строк
    assert len(df) == 3

    # Проверяем сортировку по времени
    assert df["time"].is_monotonic_increasing

    # Проверяем соответствие времени и температуры
    assert df.iloc[0]["temperature_c"] == 1.0
    assert df.iloc[1]["temperature_c"] == 2.0
    assert df.iloc[2]["temperature_c"] == 3.0