import interface
import datos
import config
import logica

def gestionar_aplicacio():
    interface.mostrar_benvinguda()
    actiu = True
    while actiu:
        interface.mostrar_menu_principal()
        opcio = interface.demanar_opcio()
        if opcio == "1":
            interface.mostrar_carta_bars(datos.obtenir_tots_els_bars())
        elif opcio == "2":
            zona = interface.demanar_zona_cerca()
            trobats = datos.filtrar_bars_per_zona(zona)
            if trobats:
                interface.mostrar_carta_bars(trobats)
            else:
                interface.no_hay_bar(zona)
        elif opcio == "3":
            reserva = interface.demanar_dades_reserva()
            if reserva:
                bar = datos.cercar_bar_per_id(reserva["id_bar"])
                if not bar:
                    interface.no_existe_bar()
                elif not datos.validar_disponibilitat(bar["aforament_actual"], reserva["persones"], bar["aforament_max"]):
                    interface.mensaje_error(config.MSG_ERROR_AFORAMENT)
                else:
                    detall = logica.calcular_total_comanda(bar["preu_tapa"], reserva["tapes"], reserva["persones"], reserva["es_soci"])
                    datos.actualitzar_dades_bar(bar["id"], reserva["persones"], reserva["tapes"])
                    interface.mostrar_resum_comanda(bar, reserva, detall)
        elif opcio == "4":
            stats = datos.calcular_estadistiques_globals(datos.obtenir_tots_els_bars())
            interface.mostrar_panell_estadistiques(stats)
        elif opcio == "0":
            interface.adios()
            actiu = False
        else:
            interface.mensaje_error(config.MSG_OPCIO_INVALIDA)

if __name__ == "__main__":
    gestionar_aplicacio()