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

def obtenir_tots_els_bars():
    return inventari_bars

def cercar_bar_per_id(id_buscat):
    for bar in inventari_bars:
        if bar["id"] == id_buscat:
            return bar
    return None

def filtrar_bars_per_zona(zona_cercada):
    coincidencies = []
    for bar in inventari_bars:
        if bar["zona"].lower() == zona_cercada.strip().lower():
            coincidencies.append(bar)
    return coincidencies

def actualitzar_dades_bar(id_bar, noves_persones, noves_tapes):
    bar = cercar_bar_per_id(id_bar)
    if bar:
        bar["aforament_actual"] += noves_persones
        bar["tapes_venudes"] += noves_tapes
        return True
    return False

def validar_disponibilitat(aforament_actual, persones, aforament_maxim):
    return (aforament_actual + persones) <= aforament_maxim

def calcular_descompte(subtotal, quantitat_persones, es_soci):
    print(">> Verificant promocions aplicables a la comanda...")
    if es_soci:
        return subtotal * DESCOMPTE_SOCI
    elif quantitat_persones >= MIN_PERSONES_GRUP:
        return subtotal * DESCOMPTE_GRUP
    return 0.0

def calcular_total_comanda(preu_tapa, quantitat_tapes, quantitat_persones, es_soci):
    print(">> Calculant import econòmic amb desglossament d'IVA...")
    subtotal_brut = preu_tapa * quantitat_tapes
    import_descompte = calcular_descompte(subtotal_brut, quantitat_persones, es_soci)
    base_imposable = subtotal_brut - import_descompte
    quota_iva = base_imposable * IVA_HOSTALERIA
    total_final = base_imposable + quota_iva
    return {
        "subtotal_brut": round(subtotal_brut, 2), "descompte": round(import_descompte, 2),
        "base_imposable": round(base_imposable, 2), "iva": round(quota_iva, 2), "total": round(total_final, 2)
    }

def calcular_estadistiques_globals(llista_bars):
    print(">> Calculant mètriques de rendiment de la xarxa...")
    if not llista_bars:
        return None
    total_tapes = sum(b["tapes_venudes"] for b in llista_bars)
    preu_mig = sum(b["preu_tapa"] for b in llista_bars) / len(llista_bars)
    bar_top = max(llista_bars, key=lambda b: b["tapes_venudes"])
    return {
        "num_bars": len(llista_bars), "total_tapes": total_tapes,
        "preu_mitja": round(preu_mig, 2), "bar_popular": bar_top["nom"]
    }

def mostrar_benvinguda():
    print("=" * 55)
    print(f"🌟  {NOM_ESDEVENIMENT} (v{VERSIO})")
    print("=" * 55)

def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Catàleg de bars i preus")
    print("2. Cercar bars per zona")
    print("3. Reservar taula i demanar tapes")
    print("4. Estadístiques de la xarxa")
    print("0. Sortir")

def demanar_opcio():
    return input("\n👉 Selecciona una opció: ").strip()

def mostrar_carta_bars(llista):
    print("\n📍 LOCALS DISPONIBLES:")
    for b in llista:
        lliures = b["aforament_max"] - b["aforament_actual"]
        print(f"  [{b['id']}] {b['nom']:<26} | {b['zona']:<9} | {b['preu_tapa']:.2f}€ | Lliures: {lliures}")

def demanar_zona_cerca():
    return input("\n👉 Introdueix la zona a cercar: ").strip()

def demanar_dades_reserva():
    try:
        id_bar = int(input("\n👉 ID del bar: "))
        persones = int(input("👉 Nombre de persones: "))
        tapes = int(input("👉 Nombre de tapes: "))
        soci = input("👉 Ets soci/a del festival? (s/n): ").strip().lower() == "s"
        if persones <= 0 or persones > MAX_PERSONES_RESERVA or tapes <= 0:
            print("❌ Valors fora de rang permès.")
            return None
        return {"id_bar": id_bar, "persones": persones, "tapes": tapes, "es_soci": soci}
    except ValueError:
        print("❌ Error: Cal introduir valors numèrics enters.")
        return None

def mostrar_resum_comanda(bar, reserva, detall):
    print("\n" + "=" * 45)
    print(f"🧾 REBUT DE RESERVA: {bar['nom'].upper()}")
    print("-" * 45)
    print(f"Persones: {reserva['persones']} | Tapes: {reserva['tapes']}")
    print(f"Subtotal: {detall['subtotal_brut']:.2f}€ | Descompte: -{detall['descompte']:.2f}€")
    print(f"Base: {detall['base_imposable']:.2f}€ | IVA (10%): {detall['iva']:.2f}€")
    print("-" * 45)
    print(f"💰 TOTAL: {detall['total']:.2f}€")
    print("=" * 45)
    print(MSG_EXIT_RESERVA)

def mostrar_panell_estadistiques(stats):
    if not stats:
        print("❌ No hi ha dades suficients.")
        return
    print("\n📊 ESTADÍSTIQUES DEL CIRCUIT:")
    print(f"  • Total bars: {stats['num_bars']} | Tapes venudes: {stats['total_tapes']}")
    print(f"  • Preu mitjà: {stats['preu_mitja']:.2f}€ | Més popular: {stats['bar_popular']}")

def gestionar_aplicacio():
    mostrar_benvinguda()
    actiu = True
    while actiu:
        mostrar_menu_principal()
        opcio = demanar_opcio()
        if opcio == "1":
            mostrar_carta_bars(obtenir_tots_els_bars())
        elif opcio == "2":
            zona = demanar_zona_cerca()
            trobats = filtrar_bars_per_zona(zona)
            if trobats:
                mostrar_carta_bars(trobats)
            else:
                print(f"❌ No s'ha trobat cap bar a '{zona}'.")
        elif opcio == "3":
            reserva = demanar_dades_reserva()
            if reserva:
                bar = cercar_bar_per_id(reserva["id_bar"])
                if not bar:
                    print("❌ No existeix aquest bar.")
                elif not validar_disponibilitat(bar["aforament_actual"], reserva["persones"], bar["aforament_max"]):
                    print(MSG_ERROR_AFORAMENT)
                else:
                    detall = calcular_total_comanda(bar["preu_tapa"], reserva["tapes"], reserva["persones"], reserva["es_soci"])
                    actualitzar_dades_bar(bar["id"], reserva["persones"], reserva["tapes"])
                    mostrar_resum_comanda(bar, reserva, detall)
        elif opcio == "4":
            stats = calcular_estadistiques_globals(obtenir_tots_els_bars())
            mostrar_panell_estadistiques(stats)
        elif opcio == "0":
            print(f"\nGràcies per utilitzar {NOM_ESDEVENIMENT}. Fins aviat!")
            actiu = False
        else:
            print(MSG_OPCIO_INVALIDA)

if __name__ == "__main__":
    gestionar_aplicacio()
