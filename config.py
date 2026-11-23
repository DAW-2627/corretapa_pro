"""
Sistema de Gestió - Corretapa Pro
Aplicació per a la gestió de reserves, comandes de tapes i estadístiques.
"""

NOM_ESDEVENIMENT = "Corretapa Pro Barcelona"
VERSIO = "2.1.0"
IVA_HOSTALERIA = 0.10
DESCOMPTE_SOCI = 0.15
DESCOMPTE_GRUP = 0.10
MIN_PERSONES_GRUP = 5
MAX_PERSONES_RESERVA = 20
MSG_ERROR_AFORAMENT = "❌ No queden suficients places disponibles al local seleccionat."
MSG_EXIT_RESERVA = "🎉 Reserva i comanda de tapes confirmades amb èxit!"
MSG_OPCIO_INVALIDA = "❌ Opció no vàlida. Introdueix un número de la llista."

inventari_bars = [
    {"id": 1, "nom": "El Racó del Born", "zona": "Born", "preu_tapa": 3.50, "aforament_actual": 38, "aforament_max": 50, "tapes_venudes": 140},
    {"id": 2, "nom": "Taverna Central Gràcia", "zona": "Gràcia", "preu_tapa": 2.80, "aforament_actual": 22, "aforament_max": 30, "tapes_venudes": 95},
    {"id": 3, "nom": "Craft & Tapes Poblenou", "zona": "Poblenou", "preu_tapa": 3.20, "aforament_actual": 15, "aforament_max": 40, "tapes_venudes": 160},
    {"id": 4, "nom": "Cerveseria de la Cantonada", "zona": "Sants", "preu_tapa": 2.50, "aforament_actual": 28, "aforament_max": 35, "tapes_venudes": 80},
    {"id": 5, "nom": "El Nou Bar Musical", "zona": "Raval", "preu_tapa": 3.00, "aforament_actual": 12, "aforament_max": 25, "tapes_venudes": 110}
]
