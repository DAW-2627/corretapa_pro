import interface
import config
import logic
import dades_bars


def gestionar_aplicacio():
    interface.mostrar_benvinguda()
    actiu = True
    while actiu:
        interface.mostrar_menu_principal()
        opcio = interface.demanar_opcio()
        if opcio == "1":
            interface.mostrar_carta_bars(logic.obtenir_tots_els_bars())
        elif opcio == "2":
            zona = interface.demanar_zona_cerca()
            trobats = logic.filtrar_bars_per_zona(zona)
            if trobats:
                interface.mostrar_carta_bars(trobats)
            else:
                print(f"❌ No s'ha trobat cap bar a '{zona}'.")
        elif opcio == "3":
            reserva = interface.demanar_dades_reserva()
            if reserva:
                bar = logic.cercar_bar_per_id(reserva["id_bar"])
                if not bar:
                    print("❌ No existeix aquest bar.")
                elif not logic.validar_disponibilitat(bar["aforament_actual"], reserva["persones"], bar["aforament_max"]):
                    print(config.MSG_ERROR_AFORAMENT)
                else:
                    detall = logic.calcular_total_comanda(bar["preu_tapa"], reserva["tapes"], reserva["persones"], reserva["es_soci"])
                    logic.actualitzar_dades_bar(bar["id"], reserva["persones"], reserva["tapes"])
                    interface.mostrar_resum_comanda(bar, reserva, detall)
        elif opcio == "4":
            stats = logic.calcular_estadistiques_globals(logic.obtenir_tots_els_bars())
            interface.mostrar_panell_estadistiques(stats)
        elif opcio == "0":
            print(f"\nGràcies per utilitzar {config.NOM_ESDEVENIMENT}. Fins aviat!")
            actiu = False
        else:
            print(config.MSG_OPCIO_INVALIDA)


if __name__ == "__main__":
    gestionar_aplicacio()
