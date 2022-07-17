from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


def get_solar(visszateresi_ev: int, datum, ido, idozona, geopos_lat, geopos_lon, uj_geopos_lat=None,
              uj_geopos_lon=None):
    """
    :return: Egy dátum ami megadja a pontos idejét az év szolár képletének

    # idozona = '1'
    # date = Datetime('2001/08/19', '16:54', f'+0{idozona}:00')
    # pos = GeoPos('47n11', '20e12')  # HUN Szolnok
    """
    if uj_geopos_lat or uj_geopos_lon == False:
        uj_geopos_lat = geopos_lat
        uj_geopos_lon = geopos_lon
    print("[2] datum, ido", datum, ido)
    date = Datetime(datum, ido, f'+0{idozona}:00')
    # date = Datetime('2001/08/19', '16:54', '+02:00')

    print(geopos_lat, geopos_lon)
    pos = GeoPos(geopos_lat, geopos_lon)
    # pos = GeoPos('47n11', '20e12')
    print("~~~",date, pos, 'Placidus', const.LIST_SEVEN_PLANETS)
    chart = Chart(date, pos)

    solar = chart.solarReturn(visszateresi_ev, GeoPos(uj_geopos_lat, uj_geopos_lon))
    print(solar.date)
    # print(solar.get(const.MOON))
    # print(solar.get(const.SUN))

    return solar.date


if __name__ == '__main__':
    print(get_solar(2002, '2001/08/19', '16:54', '1', '47n11', '20e12'))
