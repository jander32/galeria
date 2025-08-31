#!/usr/bin/env python3
"""Aplicación de consola para dejar tabaco y alcohol."""

import argparse
import json
import os
import datetime

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "cigarettes_avoided": 0,
            "drinks_avoided": 0,
            "days_without": 0,
            "money_saved": 0.0,
            "diary": [],
            "achievements": [],
        }
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def register_day(data):
    print("\n--- Registro diario ---")
    cig = int(input("Cigarrillos evitados hoy: ") or 0)
    drink = int(input("Bebidas evitadas hoy: ") or 0)
    money = float(input("Dinero ahorrado hoy (€): ") or 0)
    data["cigarettes_avoided"] += cig
    data["drinks_avoided"] += drink
    data["money_saved"] += money
    if cig >= 0 and drink >= 0:
        data["days_without"] += 1
    check_achievements(data)
    save_data(data)


def check_achievements(data):
    milestones = {1: "¡Primer día sin consumir!", 7: "¡Una semana!", 30: "¡Un mes completo!"}
    if data["days_without"] in milestones and milestones[data["days_without"]] not in data["achievements"]:
        msg = milestones[data["days_without"]]
        data["achievements"].append(msg)
        print(f"\n🏅 {msg}")


def show_stats(data):
    print("\n--- Estadísticas ---")
    print(f"Días sin consumir: {data['days_without']}")
    print(f"Cigarrillos evitados: {data['cigarettes_avoided']}")
    print(f"Bebidas evitadas: {data['drinks_avoided']}")
    print(f"Dinero ahorrado: €{data['money_saved']:.2f}")


def motivational_diary(data):
    print("\n--- Diario de motivación ---")
    choice = input("(E)scribir o (V)er entradas?: ").strip().lower()
    if choice.startswith('e'):
        text = input("Escribe tu mensaje motivador: ")
        data["diary"].append({
            "date": datetime.date.today().isoformat(),
            "text": text,
        })
        save_data(data)
    else:
        for entry in data["diary"]:
            print(f"[{entry['date']}] {entry['text']}")


def emergency_corner():
    print("\n--- Rincón de emergencias ---")
    print("Respira profundo: inhalar 4s, mantener 4s, exhalar 4s. Repite 5 veces.")
    print("Recuerda por qué empezaste este camino. ¡Tú puedes!")


def run_app(data):
    while True:
        print("\n=== Freedom Tracker ===")
        print("1. Registrar día")
        print("2. Ver estadísticas")
        print("3. Diario de motivación")
        print("4. Rincón de emergencias")
        print("5. Salir")
        choice = input("> ").strip()
        if choice == '1':
            register_day(data)
        elif choice == '2':
            show_stats(data)
        elif choice == '3':
            motivational_diary(data)
        elif choice == '4':
            emergency_corner()
        elif choice == '5':
            break
        else:
            print("Opción no válida.")


def demo():
    data = load_data()
    print("Demostración rápida:")
    show_stats(data)
    emergency_corner()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="App de apoyo para dejar tabaco y alcohol")
    parser.add_argument("--demo", action="store_true", help="Ejecutar demostración y salir")
    args = parser.parse_args()
    data = load_data()
    if args.demo:
        demo()
    else:
        run_app(data)
