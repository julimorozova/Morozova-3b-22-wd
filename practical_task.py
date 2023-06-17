# Написать программу, которая в качестве входных данных принимает список кортежей, представляющих IP-адреса,
# и возвращает список уникальных сетевых адресов

def get_unique_network_addresses(ip_addresses):
    unique_addresses = set()  # Создание пустого множества для хранения уникальных сетевых адресов

    for ip_tuple in ip_addresses:  # Обработка каждого кортежа IP-адреса
        ip_address = ip_tuple[0]  # Извлечение IP-адреса из кортежа
        network_address = get_network_address(ip_address)  # Получение сетевого адреса из IP-адреса

        if network_address is not None:  # Проверка, что сетевой адрес не является некорректным
            unique_addresses.add(network_address)  # Добавление сетевого адреса во множество уникальных адресов

    return list(unique_addresses)  # Преобразование множества уникальных адресов в список и возвращение его


def get_network_address(ip_address):
    parts = ip_address.split('.')  # Разделение IP-адреса на октеты
    if len(parts) != 4:  # Проверка наличия 4-х октетов
        print(f"Некорректный IP-адрес: {ip_address}")
        return None

    network_address_parts = parts[:3] + ['0']  # Замена последнего октета на 0, чтобы получить сетевой адрес, так как последний октет отвечает за устойства в сети
    network_address = '.'.join(network_address_parts)  # Объединение октетов обратно в сетевой адрес

    return network_address


ip_addresses = [
    ('192.168.0',),
    ('10.0.0.1',),
    ('172.16.0.1',),
    ('8.8.8.8',),
    ('172.16.0.4',),
]

unique_network_addresses = get_unique_network_addresses(
    ip_addresses)  # Вызов функции для получения уникальных сетевых адресов
print(unique_network_addresses)  # Вывод списка уникальных сетевых адресов
