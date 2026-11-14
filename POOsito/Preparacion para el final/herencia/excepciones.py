# ── Excepciones del dominio ────────────────────────────────────────────────

class RentalError(Exception):
    """Base de todos los errores del dominio de Rental Ruedas."""

class VehiculoNoEncontrado(RentalError):
    """Se lanza cuando se busca una placa que no existe en el catálogo."""

class VehiculoNoDisponible(RentalError):
    """Se lanza cuando se intenta alquilar un vehículo ya reservado,
    o devolver uno que no estaba alquilado."""

class DiasInvalidos(RentalError):
    """Se lanza cuando se pide un alquiler por 0 días o menos."""

class PlacaDuplicada(RentalError):
    """Se lanza al intentar agregar al catálogo una placa ya existente."""