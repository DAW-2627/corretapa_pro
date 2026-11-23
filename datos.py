import config
import interface

def obtenir_tots_els_bars():
    return config.inventari_bars

def cercar_bar_per_id(id_buscat):
    for bar in config.inventari_bars:
        if bar["id"] == id_buscat:
            return bar
    return None

def filtrar_bars_per_zona(zona_cercada):
    coincidencies = []
    for bar in config.inventari_bars:
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

def calcular_estadistiques_globals(llista_bars):
    interface.mensaje_estadisticas_globales
    if not llista_bars:
        return None
    total_tapes = sum(b["tapes_venudes"] for b in llista_bars)
    preu_mig = sum(b["preu_tapa"] for b in llista_bars) / len(llista_bars)
    bar_top = max(llista_bars, key=lambda b: b["tapes_venudes"])
    return {
        "num_bars": len(llista_bars), "total_tapes": total_tapes,
        "preu_mitja": round(preu_mig, 2), "bar_popular": bar_top["nom"]
    }
