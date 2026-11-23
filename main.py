from config import MSG_ERROR_AFORAMENT, NOM_ESDEVENIMENT, MSG_OPCIO_INVALIDA
from logica_promo import calcular_estadistiques_globals, validar_disponibilitat, calcular_total_comanda
from dades_bars import cercar_bar_per_id, obtenir_tots_els_bars, filtrar_bars_per_zona, actualitzar_dades_bar
from interficie import mostrar_error_zona, mostrar_error_inexistente, mostrar_error_aforament, mostrar_error_opcio, mostrar_comiat, mostrar_avis mostrar_menu_principal, mostrar_benvinguda, demanar_opcio, mostrar_carta_bars, demanar_zona_cerca, mostrar_panell_estadistiques, mostrar_resum_comanda, demanar_dades_reserva

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
                mostrar_error_zona(zona)
        elif opcio == "3":
            reserva = demanar_dades_reserva()
            if reserva:
                bar = cercar_bar_per_id(reserva["id_bar"])
                if not bar:
                    mostrar_error_inexistente()
                elif not validar_disponibilitat(bar["aforament_actual"], reserva["persones"], bar["aforament_max"]):
                    mostrar_error_aforament()
                else:
                    mostrar_avis(">> Verificant promocions aplicables a la comanda...")
                    mostrar_avis(">> Calculant import econòmic amb desglossament d'IVA...")
                    detall = calcular_total_comanda(bar["preu_tapa"], reserva["tapes"], reserva["persones"], reserva["es_soci"])
                    actualitzar_dades_bar(bar["id"], reserva["persones"], reserva["tapes"])
                    mostrar_resum_comanda(bar, reserva, detall)
        elif opcio == "4":
            mostrar_avis(">> Calculant mètriques de rendiment de la xarxa...")
            stats = calcular_estadistiques_globals(obtenir_tots_els_bars())
            mostrar_panell_estadistiques(stats)
        elif opcio == "0":
            mostrar_comiat()
            actiu = False
        else:
            mostrar_error_opcio()
if __name__ == "__main__":
    gestionar_aplicacio()
