from .simpson import simpson_formula
from .trapezoidal import trapezoidal_formula
from .gl import gauss_legendre_formula
from .gl import gauss_legendre_formula_intervals
from .approximation import approximate_integral

__all__ = ['simpson_formula', 'trapezoidal_formula',
           'gauss_legendre_formula', 'gauss_legendre_formula_intervals', 'approximate_integral']
