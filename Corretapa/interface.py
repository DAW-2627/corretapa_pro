NOM_ESDEVENIMENT = "Corretapa Pro Barcelona"
VERSIO = "2.1.0"
MSG_ERROR_AFORAMENT = "❌ No queden suficients places disponibles al local seleccionat."
MSG_EXIT_RESERVA = "🎉 Reserva i comanda de tapes confirmades amb èxit!"
MSG_OPCIO_INVALIDA = "❌ Opció no vàlida. Introdueix un número de la llista."

from datos import obtenir_tots_els_bars
from datos import filtrar_bars_per_zona
from datos import cercar_bar_per_id
from datos import actualitzar_dades_bar
from logica import MAX_PERSONES_RESERVA
from logica import validar_disponibilitat
from logica import calcular_total_comanda
from logica import calcular_estadistiques_globals

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