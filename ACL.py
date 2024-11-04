# Sistema heredado que administra eventos. Utiliza una estructura de datos antigua y un formato diferente de fechas y entradas.
class LegacyEventSystem:
    def get_event_info(self):
        # Devuelve los datos en un formato antiguo
        return {
            "titulo_evento": "Concierto de Jazz Clásico",
            "fecha_evento": "15/05/2024",  # Formato de fecha: DD/MM/YYYY
            "ubicacion": "Teatro Principal",
            "capacidad_total": 300,
            "entradas_disponibles": 75,
            "detalles": "Un concierto único con los mejores músicos de jazz."
        }

# Anti-Corruption Layer (EventAdapter) que adapta la información del evento al formato moderno
class EventAdapter:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def fetch_event_details(self):
        """
        Obtiene la información del evento del sistema heredado,
        traduce las claves y ajusta los formatos de datos necesarios para el sistema moderno.
        """
        try:
            legacy_data = self.legacy_system.get_event_info()
            return self._convert_to_modern_format(legacy_data)
        except KeyError as e:
            print(f"Error: Clave faltante en los datos del sistema heredado: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado al adaptar datos del sistema heredado: {e}")
            return None

    def _convert_to_modern_format(self, data):
        """
        Traduce los datos del sistema heredado al formato que necesita el sistema moderno.
        Convierte las claves y ajusta los formatos de fecha y números.
        """
        try:
            # Convertir la fecha de DD/MM/YYYY a YYYY-MM-DD
            day, month, year = data["fecha_evento"].split('/')
            formatted_date = f"{year}-{month}-{day}"

            # Calcular las entradas vendidas
            tickets_sold = data["capacidad_total"] - data["entradas_disponibles"]

            # Crear el diccionario de datos en el formato moderno
            modern_data = {
                "event_name": data["titulo_evento"],
                "event_date": formatted_date,
                "venue": data["ubicacion"],
                "total_capacity": data["capacidad_total"],
                "tickets_sold": tickets_sold,
                "available_tickets": data["entradas_disponibles"],
                "event_description": data["detalles"]
            }
            return modern_data

        except KeyError as e:
            print(f"Error: Clave faltante en los datos del sistema heredado: {e}")
            return None
        except ValueError as e:
            print(f"Error de formato en los datos del sistema heredado: {e}")
            return None

# Ejemplo de uso del Anti-Corruption Layer
legacy_event_system = LegacyEventSystem()
event_adapter = EventAdapter(legacy_event_system)

# Obtener y mostrar la información del evento en el formato moderno
event_details = event_adapter.fetch_event_details()
if event_details:
    print("Detalles del evento en formato moderno:")
    print(event_details)
