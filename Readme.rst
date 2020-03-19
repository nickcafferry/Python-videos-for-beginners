{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IPython console for SymPy 1.4 (Python 3.7.4-64-bit) (ground types: python)\n",
      "\n",
      "These commands were executed:\n",
      ">>> from __future__ import division\n",
      ">>> from sympy import *\n",
      ">>> x, y, z, t = symbols('x y z t')\n",
      ">>> k, m, n = symbols('k m n', integer=True)\n",
      ">>> f, g, h = symbols('f g h', cls=Function)\n",
      ">>> init_printing()\n",
      "\n",
      "Documentation can be found at https://docs.sympy.org/1.4/\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sympy import *\n",
    "init_session()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "@vectorize(0,1)\n",
    "def vdiff(f,y):\n",
    "    return diff(f,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\left[ \\left[ \\frac{\\partial}{\\partial x} f{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial y} f{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial z} f{\\left(x,y,z \\right)}\\right], \\  \\left[ \\frac{\\partial}{\\partial x} g{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial y} g{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial z} g{\\left(x,y,z \\right)}\\right], \\  \\left[ \\frac{\\partial}{\\partial x} h{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial y} h{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial z} h{\\left(x,y,z \\right)}\\right]\\right]$"
      ],
      "text/plain": [
       "⎡⎡∂               ∂               ∂             ⎤  ⎡∂               ∂         \n",
       "⎢⎢──(f(x, y, z)), ──(f(x, y, z)), ──(f(x, y, z))⎥, ⎢──(g(x, y, z)), ──(g(x, y,\n",
       "⎣⎣∂x              ∂y              ∂z            ⎦  ⎣∂x              ∂y        \n",
       "\n",
       "      ∂             ⎤  ⎡∂               ∂               ∂             ⎤⎤\n",
       " z)), ──(g(x, y, z))⎥, ⎢──(h(x, y, z)), ──(h(x, y, z)), ──(h(x, y, z))⎥⎥\n",
       "      ∂z            ⎦  ⎣∂x              ∂y              ∂z            ⎦⎦"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vdiff([f(x, y, z), g(x, y, z), h(x, y, z)], [x, y, z])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\left[ \\frac{\\partial}{\\partial x} s{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial y} s{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial z} s{\\left(x,y,z \\right)}\\right]$"
      ],
      "text/plain": [
       "⎡∂               ∂               ∂             ⎤\n",
       "⎢──(s(x, y, z)), ──(s(x, y, z)), ──(s(x, y, z))⎥\n",
       "⎣∂x              ∂y              ∂z            ⎦"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = symbols(\"s\",cls=Function)\n",
    "vdiff(s(x,y,z),[x,y,z])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2*C.x*C.y - C.y)*C.i + (C.x**2 - C.x)*C.j\n"
     ]
    }
   ],
   "source": [
    "from sympy.vector import CoordSys3D, gradient, Del\n",
    "# 1 gradient\n",
    "C = CoordSys3D('C')\n",
    "\n",
    "delop = Del() # nabla算子\n",
    "\n",
    "# 标量场 f = x**2*y-xy\n",
    "f = C.x**2*C.y - C.x*C.y\n",
    "\n",
    "res = delop.gradient(f, doit=True) # 使用nabla算子\n",
    "# res = delop(f).doit()\n",
    "\n",
    "res = gradient(f) # 直接使用gradient\n",
    "print(res) # (2*C.x*C.y - C.y)*C.i + (C.x**2 - C.x)*C.j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = symbols('f', cls=Function)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAKQAAAAaCAYAAAA5dfdEAAAABHNCSVQICAgIfAhkiAAABEVJREFUeJztmm2IVUUYx3/WGtiKaWuylkmhkkRkL4hgWWFiFPjFkjAiJSVCLQyLXEFYiHwriV5QUpCb9IKZFdVSmIVGomiwH0z9UrIoaCG0Zq/my/bhea6ePXvmnJl7zr1z9zI/OOw9M8/M87/Pzp3zzMyBQKCf0Axc71tEIJM2YD9wGjgJfA7c4lVRNuNNFZellC8DfqmKnECR3AesAyYDU4FzwA7gao+asrgCmOPSoA35goH+x2DgPDDDt5AMXgJuszFsAb5OKJsPfAL8BPwD/A58D8zDPNMGas9IoAe4y7eQDEYCX9gYrgEWxMqeRr7kceA9YCWwCTil5R8BA4pSGsjFFqATuNy3EAs6kJTDSBOSGI+LlU9FHgHxmbAVOIoMyocLkRjIwyvACWCsbyGWLAY+SDO4B1mtucx2y5AB+WZC3XatmxkrHwCUtG6Vli3R+yUGPzcBZ4DvHLTlwZcel5hFWQv8CtxcsB4XXLXfi4w342y+FNjjKOIFdfRaQt0EJME+FHO6VttsiJRN0rKtBj/bkRXkrY76KsWXHpeYlXkD/4MR3LUP1XLj4mYTlomm0gQc0E4fMNiUtH6u3pdn1C30TgEGAn8jKUCcWdrmdQdtefGpp4RdzEC2fE4jaVVr5BpcJW1ZlLDXDvKjnmXqrAN438H5q+qsI8VmFLIq7wIWqf1XyF5UnF1af22krBk4hswAVzloKwJfelxi1mO42qukLQsX7QDdwEJTZ98AGy0dP6vODpO9CbuSS4HaDVxpsFtB3xxkNb1/cWl0Yf4HJV3vZvSXV08ebGNWKV0UG6soLtqPAc+Xb5pilWcyGpdZiDyuDgH3A79l2J+MfJ6HPAqT2K1/JwEfI0dMzyF57TsWun4G/rWwK3M8oz6vnjzYxqxSio5VFBftzWk6NiNnoWksRkb+AWCEhbjZwAVkO6IHWJ9iO0xtd+n9DiRJvt3CTzXwpcclZvWGq/azwKOmyuXI6YuJF9VJJzDcQtxDwH/I4L0GebyfJeVwHTgI/AU8pr7WWfipJrXWU0nM6gVX7UOQmN5h6nA6kmQmsVwb/4Ddwf3dyFR9BDkmAnhE+/g0pd3bavMHMvX7fknARU+JfPllpTGrByrRPhn4k76p40UGIVsIN8bK52jH55D9xvaEa27EfgJyrHgCGBPra7/2NcWg4QkuJcTzTUJriIuezWr3eAV+8sTMN5VqXwRsy+p8PfBkrKyd7FXYTrUdi7y21k3ypvE0td9r8D9F6/dRH+fjLno6kR/0MEcfeWPmkzzatwEPZjm4Dvgyh8C8fIYsHCZ61BDFVs9QtVtTdUWNQQvwra3xy9TuiC5KeeHwlgffSbjomYFsX7RWVVHj0IbDK3IDkUPwWrznOBo5Q9+I7IP+SPGbwP1ZTyMyBnjGtVELcEPhUvryFDILdQMf0vuYzgf1pqcRudO3gEAgEAgEAoFA4/A/WeF7WYb+fgkAAAAASUVORK5CYII=\n",
      "text/latex": [
       "$\\displaystyle \\left( 2 x y - y, \\  x^{2} - x\\right)$"
      ],
      "text/plain": [
       "⎛            2    ⎞\n",
       "⎝2⋅x⋅y - y, x  - x⎠"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "diff(x**2*y-x*y,x), diff(x**2*y-x*y,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(Derivative(s(D.x, D.y, D.z), D.x))*D.i + (Derivative(s(D.x, D.y, D.z), D.y))*D.j + (Derivative(s(D.x, D.y, D.z), D.z))*D.k\n"
     ]
    }
   ],
   "source": [
    "from sympy.vector import CoordSys3D,gradient,Del\n",
    "D = CoordSys3D('D')\n",
    "delop = Del()\n",
    "s = Function('s')(D.x,D.y,D.z)\n",
    "delta_s = delop.gradient(s,doit=True)\n",
    "print(delta_s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "init_printing(use_unicode=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (\\frac{\\partial}{\\partial \\mathbf{{x}_{D}}} s{\\left(\\mathbf{{x}_{D}},\\mathbf{{y}_{D}},\\mathbf{{z}_{D}} \\right)})\\mathbf{\\hat{i}_{D}} + (\\frac{\\partial}{\\partial \\mathbf{{y}_{D}}} s{\\left(\\mathbf{{x}_{D}},\\mathbf{{y}_{D}},\\mathbf{{z}_{D}} \\right)})\\mathbf{\\hat{j}_{D}} + (\\frac{\\partial}{\\partial \\mathbf{{z}_{D}}} s{\\left(\\mathbf{{x}_{D}},\\mathbf{{y}_{D}},\\mathbf{{z}_{D}} \\right)})\\mathbf{\\hat{k}_{D}}$"
      ],
      "text/plain": [
       "(Derivative(s(D.x, D.y, D.z), D.x))*D.i + (Derivative(s(D.x, D.y, D.z), D.y))*D.j + (Derivative(s(D.x, D.y, D.z), D.z))*D.k"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "diff(s,D.x)*D.i + diff(s, D.y)*D.j +  diff(s,D.z)*D.k"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Differential Operations for Scalars, Vectors, and Tensors in Cartesian Coordinates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(Derivative(Vx(C.x), C.x))*C.i + (Derivative(Vy(C.y), C.y))*C.j + (Derivative(Vz(C.z), C.z))*C.k\n"
     ]
    }
   ],
   "source": [
    "from sympy.vector import CoordSys3D,gradient,Del\n",
    "C = CoordSys3D('C')\n",
    "Vx = Function('Vx')\n",
    "Vy = Function('Vy')\n",
    "Vz = Function('Vz')\n",
    "V = Function('Vx')(C.x) + Function('Vy')(C.y) + Function('Vz')(C.z)\n",
    "delta_V = Del().gradient(V,doit=True)\n",
    "print(delta_V)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (\\frac{d}{d \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (\\frac{d}{d \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{y}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (\\frac{d}{d \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(Derivative(Vx(C.x), C.x))*C.i + (Derivative(Vy(C.y), C.y))*C.j + (Derivative(Vz(C.z), C.z))*C.k"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(Derivative(Vx(C.x), C.x))*C.i + (Derivative(Vy(C.y), C.y))*C.j + (Derivative(Vz(C.z), C.z))*C.k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "V = Function('Vx')(C.x,C.y,C.z) + Function('Vy')(C.x,C.y,C.z) + Function('Vz')(C.x,C.y,C.z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "DiffV = Del().gradient(V,doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAIQAAAAdCAYAAABrLcQsAAAABHNCSVQICAgIfAhkiAAABHdJREFUaIHtm11oHUUUgL+mtTZCehtTsUbQvFhjCdUipfjiH60vtUSDSDUoS1ulCv5CWwqCgn9Y0YdqFR9EK4qQJ1EDRRDxQcQKLRgTbUuspaVENFpTe9PWtvHhzHBnd2fvnb37l8T9YNndM2dmztw5mZ8zmznMXFYAvep5ABgp0JY8KbTdc4ErHPRWAM+pa1mG9mjagFHgAjAFDAOtOdRbNGm126VPrbwGXNlAp4jO+UDV9TiwTT3vyrjO6UBa7b4GeCxupoeBzQ56eXfOelXHs4Zsh5Kty7Deokm73duoTT0N6QS+A+Y00Pu/ds5sYB6wF7jERfkdYEum5pRMB14CtjdSuhw4BSzJ3JySolkKnAAWakGLRek+4FdgLB+bnPCQaUhfXUUaUyAe6f4OB4Eq0KcFNofoBfbVKaQDGWqGgH/UNaRkHQkNLMmffcBd+mVeIPEiYBXwWUTmHuALwvvYHnV5wB3AjykYWhLme/xruz9TKHM/8GhUYjcyFK23pLUiQ4werv5CdhSvqGctPwAsSMFQE49yysiKR5DfdAmEp4wudZ+wZOxHAhqa+4GtyH6235AvDbxnTT9wjpqzDCAj3WzEI/0/DN3XV0PYISrq/rcl492BQvYY73uAk8Z7H/nQD+xGQuwA7yGL4n9zqn82oPu6AmGHmK/upy0ZbzCeDyMeqrmgZJrrExjoStAZdgIbgfM51D2b0H09H8IOUVX3NktGcwdhm1JM2eKmTHMn6AwvAk/gd9ISN3RfVyHsEOPqvpD62ELapizrjnmBmjNsAZ6po3sx8BTwLTI8TgKHgHeB6zK0ESSeMxXj+jBhfc20Vff1HxDedo6qe4Uw48gZh1mIrWCtmwfn8U9VQdqBL5HjeZCYySHkBHcDEj/5KUP7RrFPv1EcT1BXs23Vff1LVMG/Ac9b5IPUPHkC/+jSgiwqdfqgYyNc8fD/JY0Yz2eBOyPyfWTovYp/97ESuDVlO7PGI3qX0Wxb3wR+rlfpAPC5Rf5QwJi1RtraQNqmehU0gRcofzkSYdPvp4E1gTwVZLcxhQRfGp3czgQ87A6RpK3fAG/XU7gH+9AVDEydQIJSwcDUQcIfyLyv0rwYhpp4hH+IyxDP1rIqcIuRZ6WR9oZDHUltzAMPu0PEbaumBZlabjMFQT4FzqhKTCaR+II+9KoggamtwCIlG1M6k5aKQQJIafE7EiY/qt5bkZHtJvUed5GbhY150eyCfjVwDPi6keIDwFsRaR3Ay8incqfUNaxkUYdb+5F1R3sMY008oufObsQ5zJHrRuIPo0ltzIMN+H+Hq5S82SnjY+BBF8UW4Cvg0hjGRrEI2Q3sSKGsuLgutIq0MQ7b8TuEGS+Ku6jsRPrYeb1xLfB6XIstrEMWfUV8cNOOf/F5EvgB2XNPAU9OAxtd6EEOHI9Qa0vwRNm1rZrd+M+mnLgdf8h6JrIAeBr5RnQC6fjDyCIyj38ZSINPCAex7rXoubb1ZmT91RS2hWdJvmiHqCKdnfTwsOzTkpKSkpKk/AcPpGfmy8J34gAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle \\left( \\mathbf{\\hat{0}}, \\  \\mathbf{\\hat{k}_{C}}, \\  - \\mathbf{\\hat{j}_{C}}\\right)$"
      ],
      "text/plain": [
       "(0, C_k, (-1) C_j)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(C.i).cross(C.i), (C.i).cross(C.j),(C.i).cross(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (\\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (\\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (\\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(Derivative(Vx(C.x, C.y, C.z), C.x) + Derivative(Vy(C.x, C.y, C.z), C.x) + Derivative(Vz(C.x, C.y, C.z), C.x))*C.i + (Derivative(Vx(C.x, C.y, C.z), C.y) + Derivative(Vy(C.x, C.y, C.z), C.y) + Derivative(Vz(C.x, C.y, C.z), C.y))*C.j + (Derivative(Vx(C.x, C.y, C.z), C.z) + Derivative(Vy(C.x, C.y, C.z), C.z) + Derivative(Vz(C.x, C.y, C.z), C.z))*C.k"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "DiffV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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PBW9lnjpkrf35WzQb4mTQ26btyVVxuZt3ZYYsc4WiZN9bfMC4LdZD3g+kPIvJZ8DXs96kNQ2KrHitUdyZGze1m2JlTE5G3Rb4sW8LTlinS0yPY7PSK54f5nkjLW+5Ir3mEnOmLslN6y3RfZwO+XTf+8BnrJnuddTNoL7gC9rTK9fe/ZbreV97ZnEwC6/CzYTfvNzBr2WuOmSt3flbNBviZd9bheYtyVdxuRt3ZZYsc4WiZNdbfMZrK8z9Wvsrwburab/u2qabVRixmuP5MiYvK3bEjNDczbotsSNeVtyxDpbZHocn5Fc8f4yyRlrfckV7zGTnDF3S25Yb4uM5McoG8GdrekXAG+u5r2CsoG9GHj+UaMTmRa9ltTZlbNBvyVP9FpSx1pbloJOi8SNbVRyRK8lV3RbckW3JVd0W3JDp0XCYfuS1PH/vGRp6LakjveYyRLRbUkZ622RFrcCrwY+D9wPPG7LMpcDPwF8FPgc8C7gO48VoEgg9FpSpEvOBv2WPNFrSRFrbVkiOi0SN7ZRyRG9llzRbckV3ZZc0W3JDZ0WCYftS1LE//OSJaPbkiLeYyZLR7clNay3RXZwlvIpvw8BT503FBEROcBZzNkiIilxFvO2iIiIiIiIiIiIiIiIpM1Z/D8vEZGUOIt5W0QkJc5i3hYREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREZHM+X/rUOjd25jbcAAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle (\\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (- \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (\\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(Derivative(Vx(C.x, C.y, C.z), C.y) - Derivative(Vx(C.x, C.y, C.z), C.z) + Derivative(Vy(C.x, C.y, C.z), C.y) - Derivative(Vy(C.x, C.y, C.z), C.z) + Derivative(Vz(C.x, C.y, C.z), C.y) - Derivative(Vz(C.x, C.y, C.z), C.z))*C.i + (-Derivative(Vx(C.x, C.y, C.z), C.x) + Derivative(Vx(C.x, C.y, C.z), C.z) - Derivative(Vy(C.x, C.y, C.z), C.x) + Derivative(Vy(C.x, C.y, C.z), C.z) - Derivative(Vz(C.x, C.y, C.z), C.x) + Derivative(Vz(C.x, C.y, C.z), C.z))*C.j + (Derivative(Vx(C.x, C.y, C.z), C.x) - Derivative(Vx(C.x, C.y, C.z), C.y) + Derivative(Vy(C.x, C.y, C.z), C.x) - Derivative(Vy(C.x, C.y, C.z), C.y) + Derivative(Vz(C.x, C.y, C.z), C.x) - Derivative(Vz(C.x, C.y, C.z), C.y))*C.k"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "DiffV.cross(C.i) + DiffV.cross(C.j) + DiffV.cross(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "V1 = (Function('Vx')(C.x,C.y,C.z) + Function('Vy')(C.x,C.y,C.z) + Function('Vz')(C.x,C.y,C.z))*(C.i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (\\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (- \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(Derivative(Vx(C.x, C.y, C.z), C.z) + Derivative(Vy(C.x, C.y, C.z), C.z) + Derivative(Vz(C.x, C.y, C.z), C.z))*C.j + (-Derivative(Vx(C.x, C.y, C.z), C.y) - Derivative(Vy(C.x, C.y, C.z), C.y) - Derivative(Vz(C.x, C.y, C.z), C.y))*C.k"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().cross(V1,doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (- \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (\\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(-Derivative(Vx(C.x, C.y, C.z), C.z) - Derivative(Vy(C.x, C.y, C.z), C.z) - Derivative(Vz(C.x, C.y, C.z), C.z))*C.i + (Derivative(Vx(C.x, C.y, C.z), C.x) + Derivative(Vy(C.x, C.y, C.z), C.x) + Derivative(Vz(C.x, C.y, C.z), C.x))*C.k"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V2 = (Function('Vx')(C.x,C.y,C.z) + Function('Vy')(C.x,C.y,C.z) + Function('Vz')(C.x,C.y,C.z))*(C.j)\n",
    "Del().cross(V2,doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (\\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (- \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}}$"
      ],
      "text/plain": [
       "(Derivative(Vx(C.x, C.y, C.z), C.y) + Derivative(Vy(C.x, C.y, C.z), C.y) + Derivative(Vz(C.x, C.y, C.z), C.y))*C.i + (-Derivative(Vx(C.x, C.y, C.z), C.x) - Derivative(Vy(C.x, C.y, C.z), C.x) - Derivative(Vz(C.x, C.y, C.z), C.x))*C.j"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V3 = (Function('Vx')(C.x,C.y,C.z) + Function('Vy')(C.x,C.y,C.z) + Function('Vz')(C.x,C.y,C.z))*(C.k)\n",
    "Del().cross(V3,doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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PBW9lnjpkrf35WzQb4mTQ26btyVVxuZt3ZYYsc4WiZN9bfMC4LdZD3g+kPIvJZ8DXs96kNQ2KrHitUdyZGze1m2JlTE5G3Rb4sW8LTlinS0yPY7PSK54f5nkjLW+5Ir3mEnOmLslN6y3RfZwO+XTf+8BnrJnuddTNoL7gC9rTK9fe/ZbreV97ZnEwC6/CzYTfvNzBr2WuOmSt3flbNBviZd9bheYtyVdxuRt3ZZYsc4WiZNdbfMZrK8z9Wvsrwburab/u2qabVRixmuP5MiYvK3bEjNDczbotsSNeVtyxDpbZHocn5Fc8f4yyRlrfckV7zGTnDF3S25Yb4uM5McoG8GdrekXAG+u5r2CsoG9GHj+UaMTmRa9ltTZlbNBvyVP9FpSx1pbloJOi8SNbVRyRK8lV3RbckW3JVd0W3JDp0XCYfuS1PH/vGRp6LakjveYyRLRbUkZ622RFrcCrwY+D9wPPG7LMpcDPwF8FPgc8C7gO48VoEgg9FpSpEvOBv2WPNFrSRFrbVkiOi0SN7ZRyRG9llzRbckV3ZZc0W3JDZ0WCYftS1LE//OSJaPbkiLeYyZLR7clNay3RXZwlvIpvw8BT503FBEROcBZzNkiIilxFvO2iIiIiIiIiIiIiIiIpM1Z/D8vEZGUOIt5W0QkJc5i3hYREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREZHM+X/rUOjd25jbcAAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle (\\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (- \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (\\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(Derivative(Vx(C.x, C.y, C.z), C.y) - Derivative(Vx(C.x, C.y, C.z), C.z) + Derivative(Vy(C.x, C.y, C.z), C.y) - Derivative(Vy(C.x, C.y, C.z), C.z) + Derivative(Vz(C.x, C.y, C.z), C.y) - Derivative(Vz(C.x, C.y, C.z), C.z))*C.i + (-Derivative(Vx(C.x, C.y, C.z), C.x) + Derivative(Vx(C.x, C.y, C.z), C.z) - Derivative(Vy(C.x, C.y, C.z), C.x) + Derivative(Vy(C.x, C.y, C.z), C.z) - Derivative(Vz(C.x, C.y, C.z), C.x) + Derivative(Vz(C.x, C.y, C.z), C.z))*C.j + (Derivative(Vx(C.x, C.y, C.z), C.x) - Derivative(Vx(C.x, C.y, C.z), C.y) + Derivative(Vy(C.x, C.y, C.z), C.x) - Derivative(Vy(C.x, C.y, C.z), C.y) + Derivative(Vz(C.x, C.y, C.z), C.x) - Derivative(Vz(C.x, C.y, C.z), C.y))*C.k"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().cross(V1,doit=True) + Del().cross(V2,doit=True) + Del().cross(V3,doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Derivative(Vx(C.x, C.y, C.z), C.x) + Derivative(Vy(C.x, C.y, C.z), C.x) + Derivative(Vz(C.x, C.y, C.z), C.x)\n"
     ]
    }
   ],
   "source": [
    "from sympy.vector import CoordSys3D,gradient,Del\n",
    "C = CoordSys3D('C')\n",
    "Vx = Function('Vx')\n",
    "Vy = Function('Vy')\n",
    "Vz = Function('Vz')\n",
    "V = (Function('Vx')(C.x,C.y,C.z) + Function('Vy')(C.x,C.y,C.z) + Function('Vz')(C.x,C.y,C.z))*(C.i)\n",
    "delta_V = Del().dot(V,doit=True)\n",
    "print(delta_V)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                         ∂                         ∂                        \n",
       "────(Vx(C_x, C_y, C_z)) + ────(Vx(C_x, C_y, C_z)) + ────(Vx(C_x, C_y, C_z)) + \n",
       "∂C_x                      ∂C_y                      ∂C_z                      \n",
       "\n",
       " ∂                         ∂                         ∂                        \n",
       "────(Vy(C_x, C_y, C_z)) + ────(Vy(C_x, C_y, C_z)) + ────(Vy(C_x, C_y, C_z)) + \n",
       "∂C_x                      ∂C_y                      ∂C_z                      \n",
       "\n",
       " ∂                         ∂                         ∂                     \n",
       "────(Vz(C_x, C_y, C_z)) + ────(Vz(C_x, C_y, C_z)) + ────(Vz(C_x, C_y, C_z))\n",
       "∂C_x                      ∂C_y                      ∂C_z                   "
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Derivative(Vx(C.x, C.y, C.z), C.x) + Derivative(Vx(C.x, C.y, C.z), C.y) + Derivative(Vx(C.x, C.y, C.z), C.z) + Derivative(Vy(C.x, C.y, C.z), C.x) + Derivative(Vy(C.x, C.y, C.z), C.y) + Derivative(Vy(C.x, C.y, C.z), C.z) + Derivative(Vz(C.x, C.y, C.z), C.x) + Derivative(Vz(C.x, C.y, C.z), C.y) + Derivative(Vz(C.x, C.y, C.z), C.z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Del().dot((Vx(C.x,C.y,C.z))*C.i, doit=True) + Del().dot((Vy(C.x,C.y,C.z))*C.j,doit=True) + Del().dot((Vz(C.x,C.y,C.z))*C.k,doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (- \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (\\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (- \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(-Derivative(Vy(C.x, C.y, C.z), C.z) + Derivative(Vz(C.x, C.y, C.z), C.y))*C.i + (Derivative(Vx(C.x, C.y, C.z), C.z) - Derivative(Vz(C.x, C.y, C.z), C.x))*C.j + (-Derivative(Vx(C.x, C.y, C.z), C.y) + Derivative(Vy(C.x, C.y, C.z), C.x))*C.k"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().cross((Vx(C.x,C.y,C.z))*C.i, doit=True) + Del().cross((Vy(C.x,C.y,C.z))*C.j,doit=True) + Del().cross((Vz(C.x,C.y,C.z))*C.k,doit=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Transport Phenomena"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Algerbraic Operations for vectors and tensors in cartesian coordinates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IPython console for SymPy 1.4 (Python 3.7.4-64-bit) (ground types: python)\n",
      "\n",
      "These commands were executed:\n",
      ">>> from __future__ import division\n",
      ">>> from sympy import *\n",
      ">>> x, y, z, t = symbols('x y z t')\n",
      ">>> k, m, n = symbols('k m n', integer=True)\n",
      ">>> f, g, h = symbols('f g h', cls=Function)\n",
      ">>> init_printing()\n",
      "\n",
      "Documentation can be found at https://docs.sympy.org/1.4/\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sympy import *\n",
    "init_session()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sympy.vector import CoordSys3D\n",
    "C = CoordSys3D(\"C\")\n",
    "V, W = symbols(\"V W\")\n",
    "Vx,Vy,Vz = symbols('V(x:z)')\n",
    "Wx,Wy,Wz = symbols(\"W(x:z)\")\n",
    "V = Vx*C.i+Vy*C.j+Vz*C.k\n",
    "W = Wx*C.i+Wy*C.j+Wz*C.k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAN0AAAAWCAYAAABE65ltAAAABHNCSVQICAgIfAhkiAAABVVJREFUeJztmmuIVVUYhp+ZsqyxTKMfmVRQTClUGoUESQMVWRBBTFNGyKYiiSKQiYz60UShWQQWpl0Qp35EVlRUI2VGGA6VXbEbSZexCyVCM9KNaprpx/dtznbN2uestfaaM1OuFw6z93dZ79nvfOu6DyQkJEwYFgOjwEMOsQ9r7L2eHNM075sS/zz1jwLnlsTsUP8pntzNQDM0hKRjESE6Thr95mojbzaImw/8A3yPfHlf/AX8XOJ7ktrDXmrxL1JfXwBvM9AsDSHpCNV0nBT6HQD8AQw2iNumhF2BPHuAYYv9OOBvYJe2f7Ul5nX1nRPI7YpMeTo885qlIUx+HTPCNITm6Dhp9HtPG5td4r9K/VsKts3YR4QWoFd99xTsO9VmjkwPUnvIUWCZ4T9d7W8bdl9+F2SEF0yIht1q6y7JOQn4k31H/lg6hnC7ICNcQwjTEaCf2ixl+2zVuNh16Mo7Bus14EKLbxrwAzItn1ywn4ZM8Z8hI1SO+7WtR412tqv9mILtSOA34A1E5FHgTiPvKeydy5ffBRnhBROi4QLNeaakzc3IqHxqwRZLxxBuF2RU63QhOgLcDPRYPvnM1aNxsevQlXcMbtKAWyy+VZTPGr3qy/T+Nr3fCLQasa+qb27BdofaLgAO0+vVBf/xyD/+C0t7vvwuyAgvmBANpwC/A99aci7TnAcMeywdQ7hdkFGt04XWog33afwGas89HnXowjsGHRr0hGFvR5YY3wFtlrzZyBp8ALhR23gFOMgSu1H9Z+n9Icj6+gO9b0Fmrt5CTj7lX1vyvX34XZARXjAdhGm4VfNmFWxtGr8bmG7Ex9TRl9sFGdU6XQdhOhbRAqzVdtbofY7xqEMX3jGYoYEfGvZNau+sk7uS2vq1Hzi0JC4/4l2k9zfo/eWFmCHgeb2eCfwK/AgcHIHfxEAhz+XT26C9UA1XMHbZko/omSU+po6+3CYGiKshVKtFkK3G4xq7yuIfrzpsxMuBxv0gMoLMUd8wcDGyrn4NeLYO2Z7C9TXIksWG/ETqCP2C3cBXRtt71Q8iRhtwFzLCVeU3sbrAlWMecAki3oDh+6hBe6Ea9uvfBcBzyF5lGfCWfg8bD8TR0ZfbRGwNoVotTkGO/TuRvZS5L8vbh7h16MJrxUtIL52D9OgvlaS9Ts5iYAQZBUaBdXVil2vMUuCKwnURO5BpfiqyvNlL/SWOD78LMqotjUI0nIE8Q37KtQVZ3swviY+poy+3CzKqaQhhOk4FXta8shNZiF+HrrxW3K2JXcDter2iTvxFyCnSx8BRwOfIew7zVCnHddQ2yO9jn663IaPOUo2t92sDX34XZFQrGF8Nc3yKnJ5dqTlr68TG1tGH2wUZ1Tudr45tyDu0EeD6Bm3H1M+H14r8xGoDsobdRfn+6GxkGfc1cLTaOjX/hZKcLvW/o3+XW2L6kF8L7ERGtlmWmFB+F2RUKxgfDYt4RPN+QZbLM+vExtTRl9sFGdU7nY+O05Fl8jCwxKHtWPr58lrRzr6bXtvPYEDejw0hI8QJhu9dzV1oyTu/0PYQcLglpvgznPWR+V2QUa1gXDU0saSQ0+iELJaOIdwuyKje6Xx07KPWiXpKPsWZLJZ+vrxWtCLLjFHk2N2GE4GfkM2o7aXpeZpvvrUHOIPag6wsaX+d+kewLxOr8Lsgo1rBuGhow0LN2U6DY2bi6BjK7YKM6p3OVcdWZIaud2K628iJoV8Ib8Ikw4vIAcaZ+xl3QsKEID/AWLOfcSckNBXHArcCjyEb9U9wf6n/X+ZOSJgw5MfWg8DT1D9d/D9xJyQkJCQkJCQkJCTEwb98aQ//aFahkQAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle Vx Wx + Vy Wy + Vz Wz$"
      ],
      "text/plain": [
       "Vx⋅Wx + Vy⋅Wy + Vz⋅Wz"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V.dot(W)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAN0AAAAWCAYAAABE65ltAAAABHNCSVQICAgIfAhkiAAABVVJREFUeJztmmuIVVUYhp+ZsqyxTKMfmVRQTClUGoUESQMVWRBBTFNGyKYiiSKQiYz60UShWQQWpl0Qp35EVlRUI2VGGA6VXbEbSZexCyVCM9KNaprpx/dtznbN2uestfaaM1OuFw6z93dZ79nvfOu6DyQkJEwYFgOjwEMOsQ9r7L2eHNM075sS/zz1jwLnlsTsUP8pntzNQDM0hKRjESE6Thr95mojbzaImw/8A3yPfHlf/AX8XOJ7ktrDXmrxL1JfXwBvM9AsDSHpCNV0nBT6HQD8AQw2iNumhF2BPHuAYYv9OOBvYJe2f7Ul5nX1nRPI7YpMeTo885qlIUx+HTPCNITm6Dhp9HtPG5td4r9K/VsKts3YR4QWoFd99xTsO9VmjkwPUnvIUWCZ4T9d7W8bdl9+F2SEF0yIht1q6y7JOQn4k31H/lg6hnC7ICNcQwjTEaCf2ixl+2zVuNh16Mo7Bus14EKLbxrwAzItn1ywn4ZM8Z8hI1SO+7WtR412tqv9mILtSOA34A1E5FHgTiPvKeydy5ffBRnhBROi4QLNeaakzc3IqHxqwRZLxxBuF2RU63QhOgLcDPRYPvnM1aNxsevQlXcMbtKAWyy+VZTPGr3qy/T+Nr3fCLQasa+qb27BdofaLgAO0+vVBf/xyD/+C0t7vvwuyAgvmBANpwC/A99aci7TnAcMeywdQ7hdkFGt04XWog33afwGas89HnXowjsGHRr0hGFvR5YY3wFtlrzZyBp8ALhR23gFOMgSu1H9Z+n9Icj6+gO9b0Fmrt5CTj7lX1vyvX34XZARXjAdhGm4VfNmFWxtGr8bmG7Ex9TRl9sFGdU6XQdhOhbRAqzVdtbofY7xqEMX3jGYoYEfGvZNau+sk7uS2vq1Hzi0JC4/4l2k9zfo/eWFmCHgeb2eCfwK/AgcHIHfxEAhz+XT26C9UA1XMHbZko/omSU+po6+3CYGiKshVKtFkK3G4xq7yuIfrzpsxMuBxv0gMoLMUd8wcDGyrn4NeLYO2Z7C9TXIksWG/ETqCP2C3cBXRtt71Q8iRhtwFzLCVeU3sbrAlWMecAki3oDh+6hBe6Ea9uvfBcBzyF5lGfCWfg8bD8TR0ZfbRGwNoVotTkGO/TuRvZS5L8vbh7h16MJrxUtIL52D9OgvlaS9Ts5iYAQZBUaBdXVil2vMUuCKwnURO5BpfiqyvNlL/SWOD78LMqotjUI0nIE8Q37KtQVZ3swviY+poy+3CzKqaQhhOk4FXta8shNZiF+HrrxW3K2JXcDter2iTvxFyCnSx8BRwOfIew7zVCnHddQ2yO9jn663IaPOUo2t92sDX34XZFQrGF8Nc3yKnJ5dqTlr68TG1tGH2wUZ1Tudr45tyDu0EeD6Bm3H1M+H14r8xGoDsobdRfn+6GxkGfc1cLTaOjX/hZKcLvW/o3+XW2L6kF8L7ERGtlmWmFB+F2RUKxgfDYt4RPN+QZbLM+vExtTRl9sFGdU7nY+O05Fl8jCwxKHtWPr58lrRzr6bXtvPYEDejw0hI8QJhu9dzV1oyTu/0PYQcLglpvgznPWR+V2QUa1gXDU0saSQ0+iELJaOIdwuyKje6Xx07KPWiXpKPsWZLJZ+vrxWtCLLjFHk2N2GE4GfkM2o7aXpeZpvvrUHOIPag6wsaX+d+kewLxOr8Lsgo1rBuGhow0LN2U6DY2bi6BjK7YKM6p3OVcdWZIaud2K628iJoV8Ib8Ikw4vIAcaZ+xl3QsKEID/AWLOfcSckNBXHArcCjyEb9U9wf6n/X+ZOSJgw5MfWg8DT1D9d/D9xJyQkJCQkJCQkJCTEwb98aQ//aFahkQAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle Vx Wx + Vy Wy + Vz Wz$"
      ],
      "text/plain": [
       "Vx⋅Wx + Vy⋅Wy + Vz⋅Wz"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "W.dot(V)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "W.dot(V) == V.dot(W)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (Vy Wz - Vz Wy)\\mathbf{\\hat{i}_{C}} + (- Vx Wz + Vz Wx)\\mathbf{\\hat{j}_{C}} + (Vx Wy - Vy Wx)\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(Vy*Wz - Vz*Wy)*C.i + (-Vx*Wz + Vz*Wx)*C.j + (Vx*Wy - Vy*Wx)*C.k"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V.cross(W)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\left( Vy Wz - Vz Wy, \\  - Vx Wz + Vz Wx, \\  Vx Wy - Vy Wx\\right)$"
      ],
      "text/plain": [
       "(Vy⋅Wz - Vz⋅Wy, -Vx⋅Wz + Vz⋅Wx, Vx⋅Wy - Vy⋅Wx)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(V.cross(W)).dot(C.i), (V.cross(W)).dot(C.j), (V.cross(W)).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfYAAAAXCAYAAAD5hG0vAAAABHNCSVQICAgIfAhkiAAACFFJREFUeJztnXuIXcUdxz9JfCSuNj4oaLSt0JAawWpqNAhNu1BLtSAFSaMtQU5VGsRUSCOJxj+MtCSxWrDFZ4u4DaX1EduiprRRESWhGp+orTQY3bSNMQZM4is+0qx/zO94T+7OeczMb25y7s4HLrt35jdzZr6/35yZPWfOWUgkEolEItH3rALeAgb2d0MSiUQikUiM4nRgBLikifFMYC/wU+VG/EAacUsD29vF9hcexzlcyr5ekn+a5I8A3yqxeVHyT/E4fix6oV/btUsahRFbv37WTot0ntRhrOj4Z2CrtKOStcBOYJLHQao4GdP4J2rsZgD/B/5Hg8aW8DHwdkneH+gIfb4l/xzJW+N57Fj0Sr82a5c0CqMX+vWrdlqk86QOY0XHM6X80iqjaZi/1n/jeZAqJgC7gR01duswDZ0bcKztwB5L+peAT4DNcoyLLTaPSt43A45fRSb1DzqW65V+B7J2dSSNwuiFfv2qnRbpPNkhw+9cCWNLx1fkGBPKDFZSfckglGek/hNK8udJ/iOFtEWStqikzFeAj9h3ZbZRynSvwH5NR+ARYGFX/tck/clC2no6Ky7b5/GSdpWR4R+sPvqBWx+0tPPxmwa+Gq3FvqoeBwxJ3kpJ04wv0I+xEGLHmLZ2Ln5rC72IYdD1RYzxnuF/roR2zjc+8XytpH+npM08g1l5xNo0d6c04FxL3uHAFsxljZMK6bOkzH0lda7FtPmrhbQNUub4QtoxwPvAYxhHjwDXddV1N6NFvRJYZvnkq7BlJe0qI8M/WH30A7c+aGnn4zcNfDU6FXNJ7l/su/L9pdRXvIqlGV+gH2MhxI4xbe1c/NYWehHDoOuLGOM9I2xib+N84xPPZ0vejbYGD0iDXyrpkAZXSAMWW/Kux74aORj4APiPpcz3pcyvutL/LuknF9KKq5oj5PebCvknYvr/b2B8TT9ukPJ3NbDtJsM/WH30K6OsD1ra+fhNgxCNhiQ/k+9L5fs9xNGoipAYCyF2jMXQbohmfmsLvYhh0PVFjPGeETaxt3W+GcItnidL/gZLHtMkc60tU4lBOcYqy7E/Av6L/WrB41JuSiFtQOy3YTpW5B6xP0u+T8LcB3lOvo/DrIqGCmXyyyaXVrR/HHCr2N0s313J8A/WQfz0K1LXB03tXP2mwSD+Gp2AuS83DCyQev4GHNJlFyu+8rKhMRbCIHFjLIZ2Tf3WFgaJH8Og7wvt8Z4RNrEP0s75xieedwNv2jLOorMqsDEs+U0/v7fUcZTkPd+V/ldJn1Ny7OWMvmSRr7gyi33++MI58v1y+X5BwWYn5lEBgKOB9zCPDRxa0oYJwO+knutLbLoZxk2zoZr6fPXLadIHTe1c/aZBqEYr6PhjPXCYxSZGfEFvYsw2LovEjrFY2jXxWyyGObB80FQLbV+EjPdh3DQcqqkP2j3fuMbzFgob+A4qZOyWnxNLCm4CPqypvMgblrQdmFXPdDn2HuA8zD2Qh4HVJXWtl5+zgD9h7oksBP6BOYnYjgNwJOZEs0jaX6x/l+SDccQA8DPMSq6bgzGPLczB3CvsvldSxk2FY+ScBnxP2j3clfdCTX2++kHzPmhq5+o3DUI0ArPSzrkEc1nOdgzQiy/wjzGNcVkkdozF0A6a+S0WB5IPoLkW2r4IGe/a50po73wD7vE8ic4cvg9TMKuDdTUVhPKgHGc6ZrXyKqZz0yrKHIV5DC/fWfsI5tLGjBL7JXKM+cCFhd+LvIi5VDIRc3llF/ZLRROBh6SOsp2SLmSEXV7y0c+lD5raufpNCx+NwLzUYi9mJT0C3FZip6kR6MdYKDFjTFs7aO63NhE7hkHfF9rjPSPsXAntm2/APZ7Hi/0mW+Y4zGtkt9syFfk5prFzgWvk9+UNyv0Ts8vwh1Lm1grbH4vNYuBZ7Jc81mGEmC+2trcODWCeM9wLXNagjU3ICAtWV/1c+6ClXY6L37TwibHvYnbIvgR8HvNs6CeM3nkMuhrFiLFQYsaYdny5+K1NxI5h0PcF6I73jPCJvU3zDfjF83Sp8/4yg9ViMLWiklDynYV3Ye4zbKbZ/bA7pNy7mMXH0RW2c8X2Kfm5xGKzBvO2oI2YFdyUrvzJmEsye4CLGrSvKRlhweqin08fNLQr4uK3IZrdj6vDNca+jrnU9RpwnKTNkTr+YrHX0ihWjIUSM8Y048vVb6AXY7GJHcOgP9bBbbzXkRE+sbdlvgE/HwL8SGwWlBnk79e9vKKSUPLd9/nH9po9GxcVytTtLP52wXYn8DmLTfFVf3da8tfQcdaykk/VZp4yMsKC1UU/nz5oaFfExW+rxG5ejV0dLhqdiunnVuDLXXlPS/nZXelaGsWKsVBixpiWdj5+A70Yi03sGAb9sQ5u472OjPCJvS3zja8PAf6IWVh/oayBh2C2zD9VZqDAeMwljhHMFv6mzJYyG6h/BGgmHRFXlNjcJvl7GX2ZYzxmpTZS8dnm0PYiGWHB2lQ/3z6EateNi9+eB97B3OMKoalGUzHxvgP7izPyFz90v+1MQ6OYMRZKzBjT0M7Xb6AXY7GJHcOgP9bBbbzXkRE+sbdhvgnx4WTMprmqv+gBuFoqib3ByZUHMBsYztjfDUk40dRvR4qdz39YSiSakGIsPv1ynm5LP35C9V/znzERcx/iwdgtciDfwHDz/m5IwgkXv52HeWTo2KgtSoxlUozFpV/O023pxyTMo5N1jz9+xjcwr8SL9c74JnwRuAr4LWazwcv09qUTCT+S3xKJsUO/jPc29mM6Zg/Lifu3GW7kjxDsAO6lfjdm4sAg+S2RGDv0y3jvl34kEolEIpFIJBKJRCKRSCQSiUQikYjPp679Wpyg1bVwAAAAAElFTkSuQmCC\n",
      "text/latex": [
       "$\\displaystyle \\left( - Vy Wz + Vz Wy, \\  Vx Wz - Vz Wx, \\  - Vx Wy + Vy Wx\\right)$"
      ],
      "text/plain": [
       "(-Vy⋅Wz + Vz⋅Wy, Vx⋅Wz - Vz⋅Wx, -Vx⋅Wy + Vy⋅Wx)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(W.cross(V)).dot(C.i), (W.cross(V)).dot(C.j), (W.cross(V)).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "((V.cross(W)).dot(C.i), (V.cross(W)).dot(C.j), (V.cross(W)).dot(C.k)) == (-(W.cross(V)).dot(C.i), -(W.cross(V)).dot(C.j), -(W.cross(V)).dot(C.k))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "𝑇𝑥𝑥, 𝑇𝑥𝑦, 𝑇𝑥𝑧 = symbols(\"Tx(x:z)\")\n",
    "𝑇𝑦𝑥, 𝑇𝑦𝑦, 𝑇𝑦𝑧 = symbols(\"Ty(x:z)\")\n",
    "𝑇𝑧𝑥, 𝑇𝑧𝑦, 𝑇𝑧𝑧 = symbols(\"Tz(x:z)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "𝑇𝑥𝑥, 𝑇𝑥𝑦, 𝑇𝑥𝑧, 𝑇𝑦𝑥, 𝑇𝑦𝑦, 𝑇𝑦𝑧, 𝑇𝑧𝑥, 𝑇𝑧𝑦, 𝑇𝑧𝑧 = symbols(\"Tx(x:z), Ty(x:z), Tz(x:z)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "T = symbols(\"T\")\n",
    "T = Matrix([[𝑇𝑥𝑥, 𝑇𝑥𝑦, 𝑇𝑥𝑧],[𝑇𝑦𝑥, 𝑇𝑦𝑦, 𝑇𝑦𝑧],[𝑇𝑧𝑥, 𝑇𝑧𝑦, 𝑇𝑧𝑧]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left[\\begin{matrix}Vx\\\\Vy\\\\Vz\\end{matrix}\\right]$"
      ],
      "text/plain": [
       "⎡Vx⎤\n",
       "⎢  ⎥\n",
       "⎢Vy⎥\n",
       "⎢  ⎥\n",
       "⎣Vz⎦"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V.to_matrix(C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T*(V.to_matrix(C)) == T*V.to_matrix(C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left( \\left[\\begin{matrix}Txx Vx + Txy Vy + Txz Vz\\end{matrix}\\right], \\  \\left[\\begin{matrix}Tyx Vx + Tyy Vy + Tyz Vz\\end{matrix}\\right], \\  \\left[\\begin{matrix}Tzx Vx + Tzy Vy + Tzz Vz\\end{matrix}\\right]\\right)$"
      ],
      "text/plain": [
       "([Txx⋅Vx + Txy⋅Vy + Txz⋅Vz], [Tyx⋅Vx + Tyy⋅Vy + Tyz⋅Vz], [Tzx⋅Vx + Tzy⋅Vy + Tz\n",
       "z⋅Vz])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(T*V.to_matrix(C)).row(0), (T*V.to_matrix(C)).row(1), (T*V.to_matrix(C)).row(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left[\\begin{matrix}Txx Vx + Txy Vy + Txz Vz\\\\Tyx Vx + Tyy Vy + Tyz Vz\\\\Tzx Vx + Tzy Vy + Tzz Vz\\end{matrix}\\right]$"
      ],
      "text/plain": [
       "⎡Txx⋅Vx + Txy⋅Vy + Txz⋅Vz⎤\n",
       "⎢                        ⎥\n",
       "⎢Tyx⋅Vx + Tyy⋅Vy + Tyz⋅Vz⎥\n",
       "⎢                        ⎥\n",
       "⎣Tzx⋅Vx + Tzy⋅Vy + Tzz⋅Vz⎦"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T*V.to_matrix(C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left( \\left[\\begin{matrix}Vx\\\\Vy\\\\Vz\\end{matrix}\\right], \\  \\left[\\begin{matrix}Txx & Txy & Txz\\\\Tyx & Tyy & Tyz\\\\Tzx & Tzy & Tzz\\end{matrix}\\right]\\right)$"
      ],
      "text/plain": [
       "⎛⎡Vx⎤  ⎡Txx  Txy  Txz⎤⎞\n",
       "⎜⎢  ⎥  ⎢             ⎥⎟\n",
       "⎜⎢Vy⎥, ⎢Tyx  Tyy  Tyz⎥⎟\n",
       "⎜⎢  ⎥  ⎢             ⎥⎟\n",
       "⎝⎣Vz⎦  ⎣Tzx  Tzy  Tzz⎦⎠"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V.to_matrix(C),T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left( \\left[\\begin{matrix}Txx Vx + Tyx Vy + Tzx Vz\\end{matrix}\\right], \\  \\left[\\begin{matrix}Txy Vx + Tyy Vy + Tzy Vz\\end{matrix}\\right], \\  \\left[\\begin{matrix}Txz Vx + Tyz Vy + Tzz Vz\\end{matrix}\\right]\\right)$"
      ],
      "text/plain": [
       "([Txx⋅Vx + Tyx⋅Vy + Tzx⋅Vz], [Txy⋅Vx + Tyy⋅Vy + Tzy⋅Vz], [Txz⋅Vx + Tyz⋅Vy + Tz\n",
       "z⋅Vz])"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(V.to_matrix(C)).transpose()*T.col(0), (V.to_matrix(C)).transpose()*T.col(1), (V.to_matrix(C)).transpose()*T.col(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note: The above operations may be generalized to cylindrical coordinates by replacing (x,y,z) by (r,theta,z), and to replacing (x, y,z) by (r, theta,phi). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "@vectorize(0,1)\n",
    "def vdiff(f,y):\n",
    "    return diff(f,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\left[ \\frac{\\partial}{\\partial x} s{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial y} s{\\left(x,y,z \\right)}, \\  \\frac{\\partial}{\\partial z} s{\\left(x,y,z \\right)}\\right]$"
      ],
      "text/plain": [
       "⎡∂               ∂               ∂             ⎤\n",
       "⎢──(s(x, y, z)), ──(s(x, y, z)), ──(s(x, y, z))⎥\n",
       "⎣∂x              ∂y              ∂z            ⎦"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = symbols(\"s\",cls=Function)\n",
    "vdiff(s(x,y,z),[x,y,z])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "OR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = (Function('s')(C.x,C.y,C.z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\left( \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}, \\  \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}, \\  \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}\\right)$"
      ],
      "text/plain": [
       "⎛ ∂                       ∂                       ∂                    ⎞\n",
       "⎜────(s(C_x, C_y, C_z)), ────(s(C_x, C_y, C_z)), ────(s(C_x, C_y, C_z))⎟\n",
       "⎝∂C_x                    ∂C_y                    ∂C_z                  ⎠"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().dot(s*(C.i),doit=True), Del().dot(s*(C.j),doit=True), Del().dot(s*(C.k),doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Derivative(vx(C.x, C.y, C.z), C.x) + Derivative(vy(C.x, C.y, C.z), C.y) + Derivative(vz(C.x, C.y, C.z), C.z)\n"
     ]
    }
   ],
   "source": [
    "from sympy.vector import CoordSys3D,gradient,Del\n",
    "C = CoordSys3D('C')\n",
    "vx = Function('vx')\n",
    "vy = Function('vy')\n",
    "vz = Function('vz')\n",
    "v = Function('vx')(C.x,C.y,C.z)*(C.i) + Function('vy')(C.x,C.y,C.z)*(C.j) + Function('vz')(C.x,C.y,C.z)*(C.k)\n",
    "delta_v = Del().dot(v,doit=True)\n",
    "print(delta_v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (- \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (\\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} - \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (- \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(-Derivative(vy(C.x, C.y, C.z), C.z) + Derivative(vz(C.x, C.y, C.z), C.y))*C.i + (Derivative(vx(C.x, C.y, C.z), C.z) - Derivative(vz(C.x, C.y, C.z), C.x))*C.j + (-Derivative(vx(C.x, C.y, C.z), C.y) + Derivative(vy(C.x, C.y, C.z), C.x))*C.k"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().cross((vx(C.x,C.y,C.z))*C.i, doit=True) + Del().cross((vy(C.x,C.y,C.z))*C.j,doit=True) + Del().cross((vz(C.x,C.y,C.z))*C.k,doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                         ∂                         ∂                     \n",
       "────(vx(C_x, C_y, C_z)) + ────(vy(C_x, C_y, C_z)) + ────(vz(C_x, C_y, C_z))\n",
       "∂C_x                      ∂C_y                      ∂C_z                   "
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().dot((vx(C.x,C.y,C.z))*C.i, doit=True) + Del().dot((vy(C.x,C.y,C.z))*C.j, doit=True) + Del().dot((vz(C.x,C.y,C.z))*C.k, doit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "v = (Function('vx')(C.x,C.y,C.z)*(C.i) + Function('vy')(C.x,C.y,C.z)*(C.j) + Function('vz')(C.x,C.y,C.z)*(C.k))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                         ∂                         ∂                     \n",
       "────(vx(C_x, C_y, C_z)) + ────(vy(C_x, C_y, C_z)) + ────(vz(C_x, C_y, C_z))\n",
       "∂C_x                      ∂C_y                      ∂C_z                   "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(Del() & v).doit() # Scalar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "delta_S = Del().dot(s*(C.i),doit=True)*(C.i) + Del().dot(s*(C.j),doit=True)*(C.j) + Del().dot(s*(C.k),doit=True)*(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "                   ∂                                          ∂               \n",
       "vx(C_x, C_y, C_z)⋅────(s(C_x, C_y, C_z)) + vy(C_x, C_y, C_z)⋅────(s(C_x, C_y, \n",
       "                  ∂C_x                                       ∂C_y             \n",
       "\n",
       "                           ∂                    \n",
       "C_z)) + vz(C_x, C_y, C_z)⋅────(s(C_x, C_y, C_z))\n",
       "                          ∂C_z                  "
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "delta_S.dot(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial^{2}}{\\partial \\mathbf{{x}_{C}}^{2}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{y}_{C}}^{2}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{z}_{C}}^{2}} s{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "   2                         2                         2                   \n",
       "  ∂                         ∂                         ∂                    \n",
       "─────(s(C_x, C_y, C_z)) + ─────(s(C_x, C_y, C_z)) + ─────(s(C_x, C_y, C_z))\n",
       "    2                         2                         2                  \n",
       "∂C_x                      ∂C_y                      ∂C_z                   "
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(Del() & delta_S).doit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "delta_V = diff(v.dot(C.i),C.x)*(C.i) + diff(v.dot(C.j),C.y)*(C.j) + diff(v.dot(C.i),C.z)*(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial^{2}}{\\partial \\mathbf{{x}_{C}}^{2}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "   2                    \n",
       "  ∂                     \n",
       "─────(vx(C_x, C_y, C_z))\n",
       "    2                   \n",
       "∂C_x                    "
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(gradient(vx(C.x,C.y,C.z), coord_sys=C).dot(C.i)).dot(C.i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial^{2}}{\\partial \\mathbf{{y}_{C}}^{2}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "   2                    \n",
       "  ∂                     \n",
       "─────(vx(C_x, C_y, C_z))\n",
       "    2                   \n",
       "∂C_y                    "
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(gradient(vx(C.x,C.y,C.z), coord_sys=C).dot(C.j)).dot(C.j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial^{2}}{\\partial \\mathbf{{z}_{C}}^{2}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "   2                    \n",
       "  ∂                     \n",
       "─────(vx(C_x, C_y, C_z))\n",
       "    2                   \n",
       "∂C_z                    "
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(gradient(vx(C.x,C.y,C.z), coord_sys=C).dot(C.k)).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "v = (vx(C.x,C.y,C.z))*C.i + (vy(C.x,C.y,C.z))*C.j + (vz(C.x,C.y,C.z))*C.k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAIMAAAAXCAYAAAAoavwzAAAABHNCSVQICAgIfAhkiAAABKlJREFUaIHtml2IVVUUx39jaTNZjj4YJWMMZdJYNEmNUWPhg1EY00OENClkRvaQQmpECn08VWZR1ENUVBchyzK0DzGEmpCiZhoUmrKH0OyhRht1rCinHOf2sPbmrLPv3nfu17nnYc4fDsxZ/3XW+u9z9l774w5kyJAitgC/A1PTFjJBcQ2QB+5LW8i1wBiwLm0hExw7gEHgvDRF7AFOAk1pisjAAqQ6bExLwFykKryWloAMMfwI/AKcZQ2TFLkB6S1rAg9fAvwL9AENyCjPA3c4fg1AznDPKPtKw21z/K8E/jH+eWCzw7+tuGNAS0Bftdik8hwFJjv8ucDfymdDQjoADqs8oStXZY53gYuBxT5yiUnyauDh9w3fae7bgTPAAVTvAp43fm4F6AdG8S8cVxE18gyw0NiXEn8BXQFttcBs4LTKtdTh71LcKDArQS2HSb4zLDZxnvORLYb80sN1Gs4d1TljX2HuNyo/XXWmIi9woIi4bUQNPYhMK8eV7YUiz9YK76l8nzncTsV9lLCO+4GHnaufeGdYX2WOZhOnL+RwHBh2bA1ALzACtDpcC3AK6cmrTfBPgSmO31zD7RlH3CGixv6l/u73xEwCN6icY8Blxj4Nab/lbq+DFo1lRo/N/0qN4p4CjoTIHpNMz8t3Uzj/azxNJPIrZG51cT3+yuLiOuA/4iPgT2BOwP8cYC3wNfAH0rifgDeAtnFyhfCtym3XL/co22/A2XXQYdFFfPraSrzqVqPhV6Rie/GiSXiLuW9ERv1RZHT4sE4JvTzgc7XhPwwlVthLvDNsDfjNAPYRryTfEU0tD5WQy4flKuYQ8pJ3K9tTddIBsAj5qDb2LgoXttVoOGF8vVhJfD561NyvCvh3I+VrkOLlaxbh9YjGAxQulMaA2zy+epexmfhL6kBeZCWYjIx+G3s10cgco7BKJaWjA6mKNvZewuczlWiYhLTnYEiAPap8C7gAKTcDxHcLFkuQkj4AzET2rafxV4cG5Ah6KJQYuIL4FvMH9fcQ8dV7M9EH2m/i1xKPqdx6ZPY4fknpmIdso23efSaXD5VqaDPPfBByaETmkD5klOeBmz1+C5EPdwi4yNjuNP47A7G3G943/zcB3xM1/nNk7aE7RA/RXNmh7C+HGuMgR3znUwwziS8Y7bXM8UtCxzRkLteVcROFu4tbq9AAcC9R5QviAPIiRoFPPHw7cqQ8CFzqcHbxdaPnuW7DPejhXidq0DCy5weYjxx0We5xY1+gbC8Va4zCFuO/vET/N4l3hBPIYNFIQkcrhZ3Qd+Wq0ADwDvKNZ4/nlMdf8ucgW5Fh4CrPs/Yg4xsPN8U82+vY3YOlbod/RHGjSEerpDTuR+bgGSX4gnR6rcs36pLQ0Up5naESDc3I9Beq4nWBPfKeX4NY5SyapiMnm8+WEf984lNFe0o6SkG5C8g1hCt43dCI/DjycQ1ihbZTduGlt1NdyIe9sIS4i5DF8Q4V+4sUdJSDcjQ0Ibul7TXWUBFuAp6gNv/c0oicc/QipXcE+BkpofMqjOmW4xHGr2RJ6CgXpWpoA56k8DQ5gwe2E5xEfp/oLO6eIUOGDBkyTAj8D0qQAXZvR/knAAAAAElFTkSuQmCC\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "vx(C_x, C_y, C_z)"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v.dot(C.i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial^{2}}{\\partial \\mathbf{{x}_{C}}^{2}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{y}_{C}}^{2}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{z}_{C}}^{2}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "   2                          2                          2                    \n",
       "  ∂                          ∂                          ∂                     \n",
       "─────(vx(C_x, C_y, C_z)) + ─────(vx(C_x, C_y, C_z)) + ─────(vx(C_x, C_y, C_z))\n",
       "    2                          2                          2                   \n",
       "∂C_x                       ∂C_y                       ∂C_z                    "
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().dot(gradient(v.dot(C.i),coord_sys=C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAIMAAAAXCAYAAAAoavwzAAAABHNCSVQICAgIfAhkiAAABMdJREFUaIHtml1oHFUUx3+ppiZGGysoUtoSRGtTxSqaFo2VPlQUJT4IFmuLH1XrgxbUiljBj6dirOAnSi1qKFitrfRDRQhqNIiSGFqwrT5ItSp+1NimKmqqcePDuZc5c3fuzszuTkbo/GFh95z/3POfmXvPOXdmoUCBHLEB+BloyVvIUYoLgHHglryFXAiUgHvyFnKUYyvwI3BCniJ6gcNAc54iCjAPyQ4P5CVgFpIVXshLQIEQvgC+AY6xhknKuRqZLSs9B58OHAEGgVWGu8rDPctw+5VtOdAAbHK45wB/mvHGgbWO/xXl+wWY7olZK7pVnANAo+M/HvhDcVZnpANgv4rj+/TUGOM1YCawKMp5pQmyznPwZuPvBOab75s93F5gDDhX2YaMLapxXEFwkv8Clxj7YsIXoMsTrx6YAfyjYi12/Ncp3xgwLUMt+8l+Miwy4zwe5ZxunB9F+DqNz67qRmQ1fxvBvdZwn1K2FuQC7q4gbhPBie5DyspBZXuiwrH1wusq3nuOb5vy7chYx23Avc5niPBk8GXlpGg14wz6CAeBEcfWAAwAo0Cbsn9oBtMrpAX4Dkmzrco+y3B7Y8R9RXCyv6vvQ8DkCsfWCxermCXgTGOfgpy/9V09AVo0lho9Nv7zdRr3L+Ann7PPBNN1+Xpje9ThrjH2a5TN1t2bHO5FhDOLD/OBvwmvgN+AMzz844C7gU+AX5GT+xJ4EWiPieXDpyq27V9uVLYfgGMnQIdFF+HytZFwr1eLhu+RjB2JJ03Ay83vJqR+HUBWh8ZVhtttfs9GbuTHSDbROM9wt/sCK/QTngwbPbypwE7CmeQzgtJyV4JYUVimxhxGLvI7yrZmgnQALERuqh37bcob21o0HDLcSCwnXI/uN79XeASUkHIB8C7S/J0fwZ2Gvx/RuJ3yRqmETDwXepexlvBF6kAuZDVoRFa/HftOgpVZojxLZaWjA8mKdux+/M9nqtEwCTmffT4B9lHly8CpSLrZjdqLOtiLbLdsKXnOw2tAHkEP+wIDZxPeYu5V34cJ9yatBDdoF+WZqFY8qGLrldnn8LLSMQfZRtu4Own3YPXQ0G6OecNHaEJqyCDSpIwDl1UYcB1BWhoGTq7A3WK4UfW/GdhDcPLvI/t6PSH6CGplh7I/UyGmRg/R/UwUTiHcMNrPUoeXhY4pSC3XmbGb8t3FFTVoALiZIPN58TlyIcaAt2IGvEEJuTWGu8Tw7ojwrVfjjCB7fpCSc0T5HjL2ecr2dExciw2Gvywh/yXCE+EQslg0stDRRvkkjPr01KAB4FXkHs+II40jqWd2zIALDHeQ+PQ0GdnGDDh298HSEsd/n/KNmZjVpMZdSA2emoALMNfRFbXqstDRRrrJUI2GVqT8bUvATYwdSNPYkZBvH3lHNZlpkaZpOgnR+ViK8U8kXCrm5qQjCdI2kCsNd0G9BNim8dkUxzQhL0ferEN833bKNl56O9WF3NjTEoy7EHk0v1WN/UEOOtIgjYZmZLe0pdagM5Ht5nqklu9BGr00uBR4mPr8uaUJ+W/EAJJ6R4GvkRQ6p8ox3XQ8Snwmy0JHWiTV0A48QvhpclWwL5RGkOf4Wb6syQt2EhxG3k905iunQIECBQoU+F/gP4DJBp7Qv9SKAAAAAElFTkSuQmCC\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "vy(C_x, C_y, C_z)"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v.dot(C.j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial^{2}}{\\partial \\mathbf{{x}_{C}}^{2}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{y}_{C}}^{2}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{z}_{C}}^{2}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "   2                          2                          2                    \n",
       "  ∂                          ∂                          ∂                     \n",
       "─────(vy(C_x, C_y, C_z)) + ─────(vy(C_x, C_y, C_z)) + ─────(vy(C_x, C_y, C_z))\n",
       "    2                          2                          2                   \n",
       "∂C_x                       ∂C_y                       ∂C_z                    "
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().dot(gradient(v.dot(C.j),coord_sys=C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAIIAAAAXCAYAAADHqJcNAAAABHNCSVQICAgIfAhkiAAABK1JREFUaIHtmmtoHUUUx39JTb0x2rSCIqVKEC2mFesrisZKPtQHSvwiFLWltRUrggVfFCuKwQ9qjKCoKArSVDBabWl9oVQ0Wlo0MbRgFUGtth98pLG2Kmq08cYPZ5Y9O3fm3r337mZR9w8Dd+ecOec/uzPnnBku5MiRAZ4H9gMtWRP5n+IcYBK4IUsS5wJF4PYsSeRgM/A9cHRWBLYCh4DmrAjkAOA8JCrcnYXzuUg0eDYL5zlK8DmwD5gWdDQq4Vpkpaz2DD4Z+BMYBhqAHUbf1z5QY1eaMRssm6cDv6sxfZb8BSX7EZhTcYq1oVf5GQWaLPlRwG9KZ21KPAD2Uv69TgL9dfp4CTgJWOQSXmGcPOMZ/IqRd5rnO4EeR9tn9HrU2BFgAneRuIpwgn8DF5n+xUQn3+2dVv04ETisfC225Nco2QQwO0Uue0l/ISwydh5xCecY4XaHrNPI7B1to8/orSOMNi3Iy9tdZtwGwknuQVLJAdX3aAW/SeBl5e9dS7ZFyV5LmceNyCbTbYToQrijTh+txs6wT+EAcNDqawCGgHGgzTOuAXjKGH/SPAeYa/q3ViD2NeFEf1W/R4DpZcYmhQuVzyJwqumfgcw9kF01BVw0lhg+gf+nE7L7B/CDTzhonOlcfJ3pe8gzZhqw3uj0OuQXEC+anA/8RXTl/wKc4tE/ErgN+BD4GZnYl8BzQHsFXz58rHwH9cpy1fcdcMQU8AjQTTRlDRCt6+rh8C0SqZ14zDi8zDwXkJw1iuwMG02EtcN9HptnGvmrPqcK24guhAGP3ixgJ9EI8glhOrk1hi8XliqbY8gLfkv1PTBFPAC6kA8a2H6T0iK2Hg4/GV0nVhLNQXeZ51UO3QLwhqXvwmz8tYfGTZQWRUXgSoeuPk30EX1BHchLrAVNyK4PbN9CuCOLlEantHh0INEwsL0N//1LLRwakfns8REIriDXAccjYWY36rxp0IIUVEXgZv98AKkX9iM7zIf5RI+Rn6nfY0Sr9FbCj7OLaD2SBO5VvvWOHLT00uIxDzkqB353Gl8u1Mqh3YzZ5FMoIHljGClKJoFLHM53GL1lMR1vNLZc+b4Z+JRw4u8h53a9GAYJc2OH6n8ipv9+o399DN3jiBaHQVti6aXBYwaSu3VE7KX0FHF5HRwAVhBGPKC08BkHvgDOAM5G8tI7ls4AUmEPI5dMPQ5HDyKXTwE2AVcjtcdXlu7jSEQAuYJejkSHpcBHyImhC7gHuJ/oqp90+HYhWETe4khhDJnjCtV3kNLdkwaPY4lGvwZgjUNvPfB2jRwALkXubMrWbS8ao4eB0yxZI9GjnauNOmxOR44qQ1a/fWl0rSVfo2QTwEJqC4e7kJw7K4YuwAKLl2u3pcGjjfLvNmj9dXBoRVLelhi6qSC4wj4rAVvVFEgzkdX/cBX2jyGaHhZkxCMOqi0WVxvdhQnziI0Ccv38egK2fEemoMjSR6Zu5KOeEMNuF3LVvlnZfj8DHtWgGg7NyKloY8IcqsbFyH1DEn9MKSD/bRhCwu048A0SNufVaNMOweNUjmBp8KgWcTm0IzVd2xTx+tciWACHkONxZ3n1HDly5MiR4z+LfwBAzu7SowKj+gAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "vz(C_x, C_y, C_z)"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v.dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial^{2}}{\\partial \\mathbf{{x}_{C}}^{2}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{y}_{C}}^{2}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial^{2}}{\\partial \\mathbf{{z}_{C}}^{2}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "   2                          2                          2                    \n",
       "  ∂                          ∂                          ∂                     \n",
       "─────(vz(C_x, C_y, C_z)) + ─────(vz(C_x, C_y, C_z)) + ─────(vz(C_x, C_y, C_z))\n",
       "    2                          2                          2                   \n",
       "∂C_x                       ∂C_y                       ∂C_z                    "
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Del().dot(gradient(v.dot(C.k),coord_sys=C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlMAAAAhCAYAAAD9NC4LAAAABHNCSVQICAgIfAhkiAAAC/1JREFUeJztnX2wVVUZh58LIiDIlRgLC5k7ZcRHkzkGTKEMUzaZDX0aRTp2AqEvFQuytCn5w0yixkqzzIobM0mKjaZpDmORjFoQI44olqReDAJCwaQCFTj98a7VXmffvc9ee5+zzzqH+z4ze+496/PdZ6/fWd9rQ3syNLQBitKhqHYUJT+qG+WoYwtQBbYDHw5si6J0EqodRcmP6kY5KhkPDAcWAQeAcWHNUZSOQbWjKPlR3ShHPU8CC0MboSgdiGpHUfKjulEKMSi0ATGmA48AzwALgOeAMUEtymYl8E9gRGhDBiinI0P080MbEhjVjpIX1U7n6UY1ExYvzcw1gX7gkeCPTNhvNWxaxGCkQC8GTgBWA/8G5jUxj2bzNuAI8MXQhgxwbgd2AiMD5B1aN6DaUYoTUjsQVj+dphvVTHuQqZnJSEFdl5HQacBhZLFeMwU4EzgIHGM+TzH2TG1iHs1mDfACMt+uhGMaUlauCJB3aN2AakcpTkjtQFj9dJpuVDPtQaZmBiOL7/ZlJPSASWhO00wT5iC7KiyLgW2031SkZQLSS/hxaEMUAJ5AysvggvErSLmelTNeaN2AakdpjFDagbD66STdqGbai0zNbEQKbNpuhvON/32O2xrjFt9S2gX0Gr9rPIybhAhqDDAR2Auc5xEvictNvhen+L8eeAnYYOyE/PdxjXF7Vyz8m4H/Gr8qsDzm/wvH7znK2zmyzMlnNzAk5n8c8B8nzOUl2QHQ5+STdvU2mMeVJp33FIxfoXiFUEQ3i43b4pQ4b0LKaFaPHZqrHcivH9VOufRRrn5CageK6edB6n8f93vk2yzdaH3TXprpo1y9gIdmfmoCvDfBbySwA3gZKXiWU5Hh1y3UttK+Y9LK05JegrT2ttLYoshzTN43pvivNv4zHLe897EROETyQsCFRA/tMHCGcZ9D7QOd7XU3xTgZeMXJK96j+7jjdwh4bYm29FF+4T7LpPPtgvErFK8QiuhmuomzOiXNNchzeYunDc3SDuTXj2qnXPooVz8htQPF9LMEWJpwbTNpLfXMuxm60fqmvTTTR7l6AQ/NXGICXJbgZ1ueSaNMvcavYj5fYT7fQpgh03Em/wcS/GYQ2RanF7/7GIEUiM11bLiF6ME9hQzTPu+4XetzIw1yq5Pf72J+dzh+d5ZsxwLkR8u9bG/UXmkjNL50m3Q2FIxfoXiFUEQ3Q5Ae5bMJcT5q4nyvgC3NoIh+elHtlEXZ+gmpHShe78RZbsKuoLX1jtY3Qrtopi3qm1kmwMqY+wRkmPLvJLeMxyHz3n3ARSaNe4FjGzS4EZ6n/zx8F7AeWXTYkxDH9z4mGL81dfLvBp4menj7nf83JqRZBu9w8jwCvNG4j0K+A+v3/hbY4nKescfm/8MmpXsA2FUwboXiFcIsiunmfhPP7aWNMOF3I2UoFHn1o9ppHWXoJ5R2oLh+LF3ADSaN64mm0lqJ1jftq5kg9c1ok9mmmPs9xv3cOgl/k8jYB5E50pCsNba4c8SfILuX43Mfbye9t+EyHRmedlvELwKnpIQfCnwB+CPwL+RhbUWGwSdl5JXGn5287Xz6Jx23fxDtZinTDstsaoeDbya5F1nEhh1IDy6LPmqfSdbVm5FeUd1cbfzddRO2J17xuI8yKaIf1U652gE//XSSdqCxemcw8HMTbplHXmWh9Y3QbpoJWt88S+120dlkt4pBzr6wBk/MCNsKvovYYheIDUN+CHYjLeU0fO7jrcb/1x52rKO2cN+cEm408LATbj/wKNFQ7aUeeSVhF29WgT1Iofmt43Z1i+wA6YEecNK+m/4LFRuxYa8Jm8Wl9F9rYYehexP8PuiRZhHdvI/aSmAi8mP4EGF61y5F9KPaKU874KefTtQOFNPPEKL1SFd65lMWWt8I7aSZWQSub+4yCUxCvoi/IUOtE+rEmYsMo+00cZOG0fL0Zhq5LPPMZzs3+hXzud6rAnzuA2RapkryHLnLpxPsO4JUonHcXRfLqX3oUyk+hD4E6Q3YtC8iaqkfoX+vpSw7piK9JJv2OtLPSyliwyDkfp4qaF/F5JeUtg9FdDMasdnuPLoPWUB6Wixcq7UD+fWj2inPDhvfRz+dqB3Ir59hwG+oLaNxtL4ZuJppi/rmKpPoHOCr5v94a9LlHKQ3vRk4ETl/4RXCj07ZY99XAK9Ghu42k34uRJ776EKO9N9TJ/8p1G5Zfdz5fw+162S6iQrcJpo/KvE1J2+3pb42Fq4sOyYj23Jtvg+Tvh6oqA2TTJxfFbSxQmMVQl7dWB5HtgzbKYEbCubfbPLoR7VTrh2++ulU7UA+/YxAFjgfAT7bQJ7NROubiNCaaZv6xu4kWoEcrb+N9PVPZyAP8GngJON2rol/R508hnoa3AjDkPnMDUiLvwq8OyVskfu4zfgnzUcPBx4jepi/R75Dt4CvJZq7neq4X+dzc/TfCVKPE6ldAGiv+JkqZdgxCplbdntKy+i/2+LsBmwA+BRRT6gIFRqrEPLoxuVGE28/8qP3qozwrdAO+OtHtVOuHXn006naAX/9dCNriw4BF+RIv2zdaH0TofWNwe4csFf8UDHLqcjR9juBN8T87CK0MxPibTF+2+uk3Sy2IA/1EDIknETR+7DvlPp8gt9NRN/fPuQMDpDpm5ccv68b92mO2/cz7smy0oQ/3zP8z6h9rnuRHwCXMuzoob+okq7eBmwAWIU855OzAqZQobEKwVc3cS5w4lyYEbaV2rH51dOPaieiLDt6yNaO1U+nagf89XO38V9P8jlTS+nfcGqVbrS+idD6Bmm92pNK700JcwqyJXAfyYcK2gOt/pTgNx5pSS9ChgDHIVsl7Q2dZcK9k2g744fqGVyHVSZ+2vBpI/dxrIm7PuYePyhtbsz/MsfvECKcIkONm5A54dEeYUFE7NqV1Aovw44e8hXuIjZ0I2Wp3mhoFhUaqxB8dJPEmSaOezpyGknasWU8XkYfMu6rctgSp55+VDu1lGVHD/766VTtgJ9+BlG75T/p2p0QL0k3PXXSWFrwHrS+idD6psU8SbRAz74R/BlgrPlbBX4SxjQv7GsE4guGi5BnEdwJyELlPG9PP57aoddTA9nhQ94FgReT3qNrd+5EvsO8L1e12rGNsSqyVgDgdUQdkbMTY4dHtaPaCYHVzUlIo8Ve7hlNXw5mXX1UM6qZ/zMdeARpKC1Aes/2HT3HAX9BjNxl/m6l9g3ho5AFujuRluFmWjPdkcYwZG7/riaklbY90y6kc7dnzkYK6liPdGchix1vd9L+QwA78pDHhuHI7pHbmmxDK7CLzq/3CFtPO4+adOyrDazYdxAtgFXtCKqdiE7Wji/1dGN5DbJ7sIqcM2R3falmBNVMRFtoZjBSoBcjLczVyELDeU6Y05GhyCrSAp3u+HURvTn8l8j6kmuBb5RteAYzkTNO6p3Q68sw5NyR9chQ5kHkO+slGnXIS3x48yDZPZsy7MiLrw2TkGH5nhbZ1SjjkW3TNyHrGR4je6F6lnY+QzTFcQzRyer2/CrVTjFUO52NT51zPFFF+lfkpcegmlHNtLFmZlJ7KNsU5Mt2pzc+QPr8r51Pjs+nh3j3Xydhv8sXkO3EM+oHV0rGvpR0H/IuK58XfmZpZySyFbtq0j9s/rcn96p2iqHa6WyydDMU2flWRUafepy4qpliqGZawBxkt4NlMTJkaQvnWGRreBVZCGYrHLta3i6ka/QUYUXpNLK0AzJVWEV63lVqX8Cp2lEGIvV0M4jo9PQX6T96oppR2pZJSONoDLLTYS/RuRNdREfOb0B6DOvN57VIwbeFe1FLrVaU8NTTjmUytaO6n3P8VDvKQKSebj5GpJXd1C5GvxDVjNLmLEF6BluB+Y77JUTzq3ZqYiLR6alfIhp2vSeWpg67KgOBNO24rCXSkXv4p2pHGaik6aZC//U99lqKakY5iulCTr6tIi9vnI/sXroqpFGK0kZch+jj1pi7akdR8qGaUY5qupGj+nchO6GeAD4S1CJFCc9C5AC5l5HzpaYlhFHtKEo+VDOKoigDiF6kB72d7FfSKIqiKIqiKIqiKIqiKIqiKIqiKIqiKIqiKIqiKIqiKEph/gdHTwbbiqAdtQAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle Vx \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + Vy \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + Vz \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "    ∂                            ∂                            ∂               \n",
       "Vx⋅────(vx(C_x, C_y, C_z)) + Vy⋅────(vx(C_x, C_y, C_z)) + Vz⋅────(vx(C_x, C_y,\n",
       "   ∂C_x                         ∂C_y                         ∂C_z             \n",
       "\n",
       "      \n",
       " C_z))\n",
       "      "
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V.dot(gradient(v.dot(C.i),coord_sys=C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle Vx \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + Vy \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + Vz \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "    ∂                            ∂                            ∂               \n",
       "Vx⋅────(vy(C_x, C_y, C_z)) + Vy⋅────(vy(C_x, C_y, C_z)) + Vz⋅────(vy(C_x, C_y,\n",
       "   ∂C_x                         ∂C_y                         ∂C_z             \n",
       "\n",
       "      \n",
       " C_z))\n",
       "      "
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V.dot(gradient(v.dot(C.j),coord_sys=C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk8AAAAhCAYAAADApk9tAAAABHNCSVQICAgIfAhkiAAADD9JREFUeJztnX3QFVUdxz8PiKCgiIylhg7TmIE2mhkyhTJMWZkN2YtRpqPXN3oZ3wqztBqZxlSiphfNspfh0ZkwRdO0zCGLNDUhRkwUS1TAJCAUfCtIkdsfv3Nmz91nd+/Z3Xvv2Xvv7zOz8zz3vP527/ne834WqsnI0AYoSheiulEUf1QvSk+xCqgDzwIfC2yLonQLqhtF8Uf1ovQcBwK7AecD24AJYc1RlK5AdaMo/qhelJ7mCWB2aCMUpctQ3SiKP6oXJTfDQhsQYyrwMLAGOBt4Dhgf1KJsrgf+DYwObUifciQy9H5maEMCo7pRfFHNdJdeVCth8dLLSSbQDz0S/LEJ+63SpkUMRwrzHGAvYBHwCnBGC/NoJe8EdgJfDG1In3MrsAEYEyDv0JoB1Y2Sn5CagbC66Sa9qFaqQVO9HIIU0nubJHQE8Dqy0K6V4psObAd2MZ8PNfZMaWEerWQx8AIyb66E4yiknFwSIO/QmgHVjZKfkJqBsLrpJr2oVqpBU70MRxbObW2S0H0moVktM02YheyAsMwB1lG9qUWAg5EewU9CG6IA8DhSVoYXiFtDyvOMAnFDawZUN0oxymgGulc33aIX1Uq1aKqX5UhhTdt5cIrxv9txW2zc4ts9B4BB43elh3GTETGNByYBW4CTPeIlcbHJ99wU/zcD/wOWGTsB7jdx0q57nPhXGrf3xtJ9G/BfJ878mP8vHL/naN8Oj3lOPpuAETH/3YH/OGEubpMdAGvJfq51pJyU4VKTzgcKxK1RvBKAYpqZY9zmpMR5K1I+m/XMoft1UxXNQH/ppoxmIIxuIF95SyKkXrSOaQ9ryX6uHaljfm4CfDDBbwywHngVKXSWw5Gh1VU0tsq+Y9LK03K+EGndrabcgsbjTd7XpvgvMv7TYnnPTbjWmbBznbDLgR0kL+KbTfSFvQ4cbdxn0fhlzvS+m/wcALzm5BXvuX3K8dsB7N9GW9bS/oJ9rEnn2wXi1ihXCRTRzFQTZ1FKmouR7+UwTxu6XTdV0Az0l27KaAbC6Abylbc0QulF65j2sJb2agU89HKeCXBRgp9taSaNIg0av5r5fIn5fCNhhkMnmPzvS/CbRmRbM+absAuI7mM0UhhWZsS7kehLewoZgn3ecfuuR95lucnJ7w8xv9scv9vbbMfZyI+Ge9lep73SRmB8GWvSWVYgbo1ylUARzYxAeo/PJMT5hInz/YL2lCGkbqqgGegf3ZTRDITRTRpJ5a0TtEIvWseUpxJ1zAwT4PqY+8HI8OM/SW4JT0DmsNcC55g07gJ2LWlwGZ5n6Jz6ALAUWTA4MSPuAHANch9XE01RgDyLOjI6kMZY4GmiL+5l5//ldOa5vNvJcyfwFuO+J3L/1u/DHbDF5WRjj83/Ry1KdxuwsUC8GuUqgRkU08w9Jp7bIxttwm9CylAIQummCpqB/tJNUc1AON24ZJW3TlFUL1rHtI8gdcw4k9mKmPudxv3EjISvIDL2fmTOMyRLjC3unO+nad6jGQ5cZ8LNS/B/F349iqnIsLPb+n0JOCgl/EjgC8BfgBeRL2o1Mrw9uUleafzVydvOjZ/muP2LaNdJO+2wzKRxqHchyT3FIjasR3prWayl8ftodg163FNRzVxu/N21grbHXfPIt12E1E0VNAP9oxsfzUC1dGNpVt46RRG9aB3TfVoBD708Q+NWzpk0bwWDnEVhDY7PU4fge4gtdoHXKORHYBPSMk5iBNE89aUpYd5u/H/tYcO9NBbshSnhxgEPOeFeBh4hGoa9wCOvJOyiyzqwGSkwv3PcLu+QHSA9zW1O2r9l6CLDMjZsMWGzuICh6w3s8PJggt9HmqRnKaKZD9H44zkJ+SF8gDA9aEto3YTWDPSPbnw0A9XSDfiVt06RVy9ax3SnVsBDL3eYBCYjD+JJZBj14Iw4JyHDZBtM3KRhsjw9lzKX5Qzz2c51fsV8TjuGfxTwm1icJPY3YZLmuV0+k2DbTqTSjOPukJhP4xc+heJD4yOQlr9N+xyiVvlOhvZQ2mXHFKRHZNO+l/SzS4rYMAy5n6cK2FYzeSWl60sRzYxDbLY7bO5GFn8eEQvXT7qpgmagP3RTRjMQTjfNylsntQL59KJ1THdqBTz1cplJdBbwVfN/vPXocjzSY14J7IOch/Aa4Uef7LHqC4A3IENzK0k+p2E0suBtJ/C5JukOIMflb84IcyiN20kfc/7fTOM6l7FEhW0FrR91+LqTt9sqXxIL1y47DkG2zNp8HyJ9PU9RGyabOLcUsK9G+Uogr2YsjyHbee0w/zUlbGgVoXRTJc1A7+umjGYgjG7ylLdO4asXrWO6VyvgqRe722cBcmz9OtLXLx2NfIFPA/sZtxNN/Nsy8hjpaXAZRiHzk8uQkbA68L6EcGORNVo7gFM9077ZpJc0t7wb8CjRF/lH5Pm5hXsJ0TzsFMf9Ks/8B034mkfYfWhcvGev+Nkm7bBjT2Se2O0VzWPozojjStgAcDpRrycvNcpXAnk043Ktifcy8oO3d5PwvaqbqmkGel83ZTQDnddNkfJWFb1oHdM+O4LVMfGFXAB/M3+tsaciDaQ4hyNDkC8ihWWDcb8ZWe1/AnAM8OdYvFVIK249sl31VzluIA/bkbdlHwa8A5n//H1CuIXIroFlyKFmcxPCXIEMJ1tuAT6OzHM/GQv7A6RXAHK0/mnI8zsFeBDZBTED+BrwDRpbvnWP+4JIFD6LPTcj93i647aVoS3odtixN409oAGStyZfh+zOLGIDwPuRKS+fNQLtwFczce5HhvfHIIsXt2SE7WXdVE0z0Pu6Ca0ZyKebvOWtSnrROkboVq2Ap16GEZ0MeldKmIOQLXtbST7Izx4o9WCC34FIy/l8ZIhvArKV0bYGjzXh3kO03fCjWQZncIOJnzaNOIzGLZ5J16aEeLsi97805h4/pOykmP9Fjt8OpHFZZBhxBTK/O84jLEhD17UrqcXdDjsmkv1s7TVYwoaxSDnKGunMokb5HrSPZpI4xsRxT+xOI0k3tnzHdfaAcb8hhy0undRNVTUDvaubspqBzuqmSHlL0svEjPhzS9xHll60jonoRq3YOGX10nKeIFpYZ9+evQbY1/ytAz8LY1pT7NH88QW+RcizgG0vpAWc5y3je9A4rHp4IDt8yLuY71wT9pgW29EJbkeeYd6Xklrd2MZXHZn3B3gTUafjuMTYYWmVbjpRVntVN92smSJYveyHdDTs5Z6T9OVg1qWjdUx4rUBF9DIVeBhpGJ2N9JDtO292B/6OGLnR/F1N49u090QW1W5AWoIrGfpOvU4xCpmjv6MFaaVtnbSL4NytkzORQrqvR7ozkAX9tzpp/ymAHXnIY8NuyE6Pm1tsQyewi8Sv9gibpZtHTDr2tQFW6OuJFq32om7aWVZn0Lu66WbN+JKlF8sbkemwOnLWj7szqyp60TpG6xhAfsjXIFs090LOungF2eppORIZaqwjLc6pjt8A0Vu2fwmchRxB/812G57BdOSsjmYn4fowCjkraykyTLkdeV6DRKMKeYkPXW6neS+mHXbkxdeGychw+8QO2VWWA5GtzD9F1jc8SvOF5c1081miof9diE4ut+dH9bJu2lVWe1k33aaZvPjUM3sQVZ7/QF4SbKmaXrSOaQ9dVcdMp/FAtEORh+1OWZxA+nyuXUcVnxsP8e68bsE+xxeQbbLTsoMrbca+0HMr8l4on5dlNtPNGGTTRt2k/7r5356Sq7rJj+qme2mml5HI7rQ6MrI0MRZf9ZIP1UoHmIXsgLDMQYYkbaHcF1m1X0cWctlK5gDjbxfClTmBVFG6jWa6AZn6qyM97DqNL69U3Sj9RJZehhGd7v0SySMkqhelckxGGkPjkR0JW4jOgRggOtJ9GdI7WGo+L0EKvS3U53fUakUJS5ZuLIfQOGL7ecdPdaP0E1l6+SSRRjbRuHj8LBNG9aJUkguRXsBq4EzH/Tyi+VI73TCJ6LTSLxENp94ZS1OHU5VeJ003LkuINOQetqm6UfqNNL3UGLpGx15zTRjVi9JzDCCHCtaRA7nORHYYXRbSKEWpCFch2rgp5q66URR/VC9KTzIWOQJ/I7Jb6XHkFFZF6VdmI4e3vYqc73RUQhjVjaL4o3pRFEXpcQaRXvKzROs2FEVRFEVRFEVRFEVRFEVRFEVRFEVRFEVRFEVRFEVRFAWA/wMUlMiL3PqMjgAAAABJRU5ErkJggg==\n",
      "text/latex": [
       "$\\displaystyle Vx \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + Vy \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + Vz \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "    ∂                            ∂                            ∂               \n",
       "Vx⋅────(vz(C_x, C_y, C_z)) + Vy⋅────(vz(C_x, C_y, C_z)) + Vz⋅────(vz(C_x, C_y,\n",
       "   ∂C_x                         ∂C_y                         ∂C_z             \n",
       "\n",
       "      \n",
       " C_z))\n",
       "      "
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "V.dot(gradient(v.dot(C.k),coord_sys=C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [],
   "source": [
    "vv = (v.to_matrix(C))*((v.to_matrix(C)).transpose())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sympy.matrices.immutable.ImmutableDenseMatrix"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(vv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left[\\begin{matrix}\\operatorname{vx}^{2}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} & \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} & \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}\\\\\\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} & \\operatorname{vy}^{2}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} & \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}\\\\\\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} & \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} & \\operatorname{vz}^{2}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}\\end{matrix}\\right]$"
      ],
      "text/plain": [
       "⎡          2                                                                  \n",
       "⎢        vx (C_x, C_y, C_z)           vx(C_x, C_y, C_z)⋅vy(C_x, C_y, C_z)  vx(\n",
       "⎢                                                                             \n",
       "⎢                                               2                             \n",
       "⎢vx(C_x, C_y, C_z)⋅vy(C_x, C_y, C_z)          vy (C_x, C_y, C_z)           vy(\n",
       "⎢                                                                             \n",
       "⎢                                                                             \n",
       "⎣vx(C_x, C_y, C_z)⋅vz(C_x, C_y, C_z)  vy(C_x, C_y, C_z)⋅vz(C_x, C_y, C_z)     \n",
       "\n",
       "                                ⎤\n",
       "C_x, C_y, C_z)⋅vz(C_x, C_y, C_z)⎥\n",
       "                                ⎥\n",
       "                                ⎥\n",
       "C_x, C_y, C_z)⋅vz(C_x, C_y, C_z)⎥\n",
       "                                ⎥\n",
       "       2                        ⎥\n",
       "     vz (C_x, C_y, C_z)         ⎦"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}^{2}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂  ⎛  2               ⎞\n",
       "────⎝vx (C_x, C_y, C_z)⎠\n",
       "∂C_x                    "
      ]
     },
     "execution_count": 197,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(vv.row(0).dot(Matrix([1,0,0])),coord_sys =C,doit=False).dot(C.i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                                       \n",
       "────(vx(C_x, C_y, C_z)⋅vy(C_x, C_y, C_z))\n",
       "∂C_y                                     "
      ]
     },
     "execution_count": 198,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(vv.row(0).dot(Matrix([0,1,0])),coord_sys =C,doit=False).dot(C.j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                                       \n",
       "────(vx(C_x, C_y, C_z)⋅vz(C_x, C_y, C_z))\n",
       "∂C_z                                     "
      ]
     },
     "execution_count": 199,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(vv.row(0).dot(Matrix([0,0,1])),coord_sys =C,doit=False).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}^{2}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                                           ∂                                \n",
       "────(vx(C_x, C_y, C_z)⋅vy(C_x, C_y, C_z)) + ────(vx(C_x, C_y, C_z)⋅vz(C_x, C_y\n",
       "∂C_y                                        ∂C_z                              \n",
       "\n",
       "           ∂  ⎛  2               ⎞\n",
       ", C_z)) + ────⎝vx (C_x, C_y, C_z)⎠\n",
       "          ∂C_x                    "
      ]
     },
     "execution_count": 208,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(vv.row(0).dot(Matrix([1,0,0])),coord_sys =C,doit=False).dot(C.i) + gradient(vv.row(0).dot(Matrix([0,1,0])),coord_sys =C,doit=False).dot(C.j) + gradient(vv.row(0).dot(Matrix([0,0,1])),coord_sys =C,doit=False).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}^{2}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                                           ∂                                \n",
       "────(vx(C_x, C_y, C_z)⋅vy(C_x, C_y, C_z)) + ────(vy(C_x, C_y, C_z)⋅vz(C_x, C_y\n",
       "∂C_x                                        ∂C_z                              \n",
       "\n",
       "           ∂  ⎛  2               ⎞\n",
       ", C_z)) + ────⎝vy (C_x, C_y, C_z)⎠\n",
       "          ∂C_y                    "
      ]
     },
     "execution_count": 209,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(vv.row(1).dot(Matrix([1,0,0])),coord_sys =C,doit=False).dot(C.i) + gradient(vv.row(1).dot(Matrix([0,1,0])),coord_sys =C,doit=False).dot(C.j) + gradient(vv.row(1).dot(Matrix([0,0,1])),coord_sys =C,doit=False).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vz}^{2}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                                           ∂                                \n",
       "────(vx(C_x, C_y, C_z)⋅vz(C_x, C_y, C_z)) + ────(vy(C_x, C_y, C_z)⋅vz(C_x, C_y\n",
       "∂C_x                                        ∂C_y                              \n",
       "\n",
       "           ∂  ⎛  2               ⎞\n",
       ", C_z)) + ────⎝vz (C_x, C_y, C_z)⎠\n",
       "          ∂C_z                    "
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(vv.row(2).dot(Matrix([1,0,0])),coord_sys =C,doit=False).dot(C.i) + gradient(vv.row(2).dot(Matrix([0,1,0])),coord_sys =C,doit=False).dot(C.j) + gradient(vv.row(2).dot(Matrix([0,0,1])),coord_sys =C,doit=False).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "metadata": {},
   "outputs": [],
   "source": [
    "Txx = Function(\"Txx\")(C.x,C.y,C.z)\n",
    "Txy = Function(\"Txy\")(C.x,C.y,C.z)\n",
    "Txz = Function(\"Txz\")(C.x,C.y,C.z)\n",
    "Tyx = Function(\"Tyx\")(C.x,C.y,C.z)\n",
    "Tyy = Function(\"Tyy\")(C.x,C.y,C.z)\n",
    "Tyz = Function(\"Tyz\")(C.x,C.y,C.z)\n",
    "Tzx = Function(\"Tzx\")(C.x,C.y,C.z)\n",
    "Tzy = Function(\"Tzy\")(C.x,C.y,C.z)\n",
    "Tzz = Function(\"Tzz\")(C.x,C.y,C.z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "metadata": {},
   "outputs": [],
   "source": [
    "T = Matrix([[Txx,Txy,Txz],[Tyx,Tyy,Tyz],[Tzx,Tzy,Tzz]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAisAAAAhCAYAAAAYqutnAAAABHNCSVQICAgIfAhkiAAACx5JREFUeJztnX3QFVUdxz8PLwJiPBLjhIYMM5mBNFEpMJUyTOMfTg29R5GObbxlZWE+WGlT8UdpRE1TOpq93pxJQmw0y3KYimRSA0kdSS1JfSwMCAMTC1Dg9sfvnNlz9+77y9177/P7zNzhYc/vnP3t7u+75+zZc85CdsblyKMo/YRqQFFUB0oX8yjQBHYB76nZF0WpA9WAoqgOlC5nOjABWAUcAqbV646idBzVgKKoDpQe4nFgZd1OKEqNqAYURXWgdIBRGWznAw8BTwErgGeBKVU4VSM3Af8CJtbtyAjlbKRreVndjkQwEjQAqoO6UR3Uh8Z+vRSO/dFIYA4BJwMbgReApTnK2mecSfu7JK/TGTkHOA5c3qH9KeHcBuwGTqrbkQBlagBUB0o8I0EH3aYBjf3uIDT2B1JmXgBsMpmPArOBPwPzgPszODERuCKwbQzweeBF4JqQPA1gOMM+8rIJOZ5TkXewSj3MA7YiMXF1zb64lKUBUB0oyfS7DrpRAxr73UGh2F+MjP62DAFPk+01UhRzkFbz9hLKysuZSIv6uzX6oPg8hsTX6Jz5PSSmFpbkD1SrAVAdKO0U0YFH+RqA/q0LNPa7i7bYTxtgO5DW5hRgJtLiuQq5uEU5x/z7pxibTUgQB6fIDSCt7Sbw1QL2S03ahoD9a4H/4XdDrguk/8RJe5bqRsSvdfazFxgbSD8R+K9jc2VFfoA82SR11zYK7uOnyGyD8wuWUyZVagCSdTCEnNuhiPTXAEeALc62MnTQLRoA1UE3UHddcA/x5/xuY6d1QHUM0+Wxvxpp6eyk3IFf1yMHtyLGZg5wDGnRu08Z3zB5g63hrPbbkS7NsEFVK/EvwDHgXLN9Ma0XZ1GM/0U5HXjJ2dfiQPoHnbSjwGkV+jJM9YF6vinn6znze1TzVFmVBiBZB/NN+saI9E3ItX+ds60sHXSDBkB1kAWPajQA9dYFq4E1Ib+nTd41xk7rgOoYprtjvzK2Ik69McGuYew88/+rzP83EN5DlNZ+InJxd8TsewP+RXgC6TL8t7Ptmwm+l8Etzv5+G0i73Um7o2I/ViA3DPe3ndZAjXr6T8ugKWdbzvwe1d2oqyJJB2ORJ7y/h6S93+T9Vkhag3J00A0aANVBWjz6TwNRrDP5fkRrTDfQOqAKuj32K2EMMpDpCHBCgu00YzsMXIocyF0x+dLan2nSNsXsexB4Ev9CHHT+3p7C9zJ4s7PP48CrzfZJwGEn7R0d8MXlQuOP3f8NJZV7CNiTM69Hb92o0+rgbuS43KemicA/kK7hwZA8ZemgGzQAqoO0ePSnBlwG8HtjrqN9wojWAZ2h22K/ErIOqLoG/4Tcg7ynK2r/JvzWdhzzkVHqbuvxeeCMCPtxwKeB+4D/ICd+J/ADYFbCvqK439m3fXf6YWfbPxHRV+2HZRGtXZM3E97LlceHZ5CnnSSGab0mVXdPVkFaHVxt7Nz38PZdtheTrywdZNUAqA6K+pBGB8OMHA1YRgM/NnnWxthpHdDfsd8xliEHeGNK+8vxT8rMkuxfb9J/nqK8LbQG6s0RdpOBBxy7g8DD+N2Gl6XYVxgXOWXuQwLg18624DSvqvwAeWI75JR9J+2Dvor4sN/YJnEZ7e+vbZdoIyTtXSnK7DRpdfB2Wm/OM5Gb573EL0NQpg7SagBUB2X4kEYHI0kDIOd3o7H/UoKt1gF9FvtZWuV5f2GkGVBlWYJ0Ne02eZK6mtLan2bS/5BQ3kdpP6bjSAUSxB0hvo7WCziX/F2zY5GWsy37UvxW7XHaW/hV+TEXeaKwZW9BvhMSRh4fRiHH80RO/zyzv7Cyo+iEBorqYDJyXuyMh98gA/7eEJOnTB1k0QCoDor6UEQHHtk1AN2vgfHAL41t0rgIrQNGZuxXQtoBVW9DniB3AKcgc7BfIrqlnMV+AFleeV/M/mfTOn3tEefvfbSOIRjED54HSb/wXlq+4OzbbdVuDthV5cdZyBQ9u98HCB8rUcSHWSbPz3L66JHvRl0XWQYWPoJMUfyQyXN9jG2ZOsiiAVAdlOFDER149J8GJiIDS48DH0soT+uAERD741IWVpS0A6rORYLkSWR+P8D7kAO5vQR7gFtNeti7xwnICo32wvwOee/pButm/Pd0c53t18Ycl0vD2HspbE+hdTCV/V0YsKvCj0nIe0T3qWIt7SPDLyjgA8BH8J8a8uBR7EbdKQ1A9oGFNyLHdhC5Sb48wq5MHWTVAGS/9g3SawBUB0l4FG+sdFNdMIiMOTkKXJxQntYB1fnRNbH/qDHYRftiOmWTZkDVHOA5pBvvVYE0O9DovAL2liUm7RMhad/DP9kHkPnuIF3vR5y0L5rt85xt3445NpebjP1FKe1/SGuQ7ke6R12q8GMG7QIJ+zUK+ACwHrkpnZ5kGIFH/ht1JzUA2QcWXox/TpfHlFmmDrJqALJf+6waANVBHB7FGivdVhfcaWy2Er7OyhqkcaV1gE9fx/50pBW5CmnpTkOmQdmd2dXk3oo/VendGRxwWWryRw2oOgOZtnSA1oWuLHbRmD/mtHc5weTdGtgeXPRnSSD9M07aUUQEebq9HkTe/01OYQu+uONarFX4MYNsgZrHh0Ek9qKegNLgkf9GHaaB9YTHzr1m+/qcfkKyDoKcZ+y3EX4+y9ZBHg1A9mufVQOgOojDo1hjJUwHM4g+1jU59wPJGhhF61ThsN9etA4IMmJi/3Fk5T6A75idPQVMNf82ge+nLawHuBI5prjBimnJMqDoZGSQ5NcylP8yWrsB59TkRxqyDq76JNFPP53GasA2EJrI+1qAV+I32C8IzV0NdyDXaW5F5dehg7yxpzroDFYHpyIVvf256458tjbvykPrgB6J/fnAQ0hDZAXy1Gi/L3Ai8BdTwB7z705aP+E8CRnstxtpFe2gM93oZTEeWbL5FyWUFTVVyw5KcqdqLUKCbmqKchciA8duc8r+fQ1+ZCGLDxOQke63luxDWuI08DDir13+2QrqGVqX865SB3ZQ7XUllRdGHTrIGnsLUR1USZwOLK8A/ob4fh/+TJBerge0DuiB2B+NBOYQ0rraCLyAdM9Zzka6uZpI62u+kzaATPtqIh8gWo4sP/yVnAdXFwuQefth34fIynhkjv9WpFvtMHKOG/hP51kJdrUdJvkpoAo/spLWh1lId/KMDvnlkqSBS/C7m8fgrybrLkhVhQ6mA59D3psfQQb6JS2GWBTVQTX0gw5Anupt5fNX5KOG0B/1gMZ+NZQW+wtMZrvy3WzkRLhdze8k+t2dfRd4V6DcMj4brvjYc/8cMoXvLfW601ckaeAkZOXFJtIlfsz87a6+WIUO7EfUDiDfBqnyA2W9guqgOpJ0MA6ZDdNEek9mOHm1HqieER/7i5HR35YhpDvMBtlUZJpkExkkY2+edqSuHWRUZDU8RamTJA2AvH5pIk+aTdo/sqU6UHqdOB2Mwl859nnan+g1/pXKmYU0PqYgi+bsx5+zPYC/nO82pGVtF/DZjASwDdJVHfVaUcojTgOWs2jtXfx4IF11oPQ6cTr4AH7s76V1sO1yNP6VDrEaaUHvRL7TYPkU/rsx2+U9E3/lvCvwu/9+FShTu/+UXiJKAy6b8fUQXJBNdaD0A1E68GgfM2F/a9D4V3qAAWR1wSbyYadlyKyJL9fplKJUwLVInN8SkqY6UEYyGv9KTzCIfChqDzJr4THgvbV6pCjlsRJZpOhFZH2VeRF2qgNlJKPxryiKUiMN5IlxF9HL3CuKoiiKoiiKoiiKoiiKoiiKoiiKoiiKoiiKoiiK0gf8Hyw2YyC2PezMAAAAAElFTkSuQmCC\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Txx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Tyx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Tzx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                          ∂                          ∂                      \n",
       "────(Txx(C_x, C_y, C_z)) + ────(Tyx(C_x, C_y, C_z)) + ────(Tzx(C_x, C_y, C_z))\n",
       "∂C_x                       ∂C_y                       ∂C_z                    "
      ]
     },
     "execution_count": 245,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(T.row(0).dot((C.i).to_matrix(C)), doit=False).dot(C.i) + gradient(T.row(0).dot((C.j).to_matrix(C)), doit=False).dot(C.j) + gradient(T.row(0).dot((C.k).to_matrix(C)), doit=False).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Txy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Tyy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Tzy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                          ∂                          ∂                      \n",
       "────(Txy(C_x, C_y, C_z)) + ────(Tyy(C_x, C_y, C_z)) + ────(Tzy(C_x, C_y, C_z))\n",
       "∂C_x                       ∂C_y                       ∂C_z                    "
      ]
     },
     "execution_count": 246,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(T.row(1).dot((C.i).to_matrix(C)), doit=False).dot(C.i) + gradient(T.row(1).dot((C.j).to_matrix(C)), doit=False).dot(C.j) + gradient(T.row(1).dot((C.k).to_matrix(C)), doit=False).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{Txz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{Tyz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{Tzz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       " ∂                          ∂                          ∂                      \n",
       "────(Txz(C_x, C_y, C_z)) + ────(Tyz(C_x, C_y, C_z)) + ────(Tzz(C_x, C_y, C_z))\n",
       "∂C_x                       ∂C_y                       ∂C_z                    "
      ]
     },
     "execution_count": 247,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gradient(T.row(2).dot((C.i).to_matrix(C)), doit=False).dot(C.i) + gradient(T.row(2).dot((C.j).to_matrix(C)), doit=False).dot(C.j) + gradient(T.row(2).dot((C.k).to_matrix(C)), doit=False).dot(C.k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle (\\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{i}_{C}} + (\\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{j}_{C}} + (\\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)})\\mathbf{\\hat{k}_{C}}$"
      ],
      "text/plain": [
       "(vx(C.x, C.y, C.z))*C.i + (vy(C.x, C.y, C.z))*C.j + (vz(C.x, C.y, C.z))*C.k"
      ]
     },
     "execution_count": 255,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left[\\begin{matrix}\\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}\\\\\\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}\\\\\\operatorname{vz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}\\end{matrix}\\right]$"
      ],
      "text/plain": [
       "⎡vx(C_x, C_y, C_z)⎤\n",
       "⎢                 ⎥\n",
       "⎢vy(C_x, C_y, C_z)⎥\n",
       "⎢                 ⎥\n",
       "⎣vz(C_x, C_y, C_z)⎦"
      ]
     },
     "execution_count": 270,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v.to_matrix(C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 286,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{Txx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Txy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Txz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "                    ∂                                            ∂            \n",
       "Txx(C_x, C_y, C_z)⋅────(vx(C_x, C_y, C_z)) + Txy(C_x, C_y, C_z)⋅────(vx(C_x, C\n",
       "                   ∂C_x                                         ∂C_y          \n",
       "\n",
       "                                ∂                     \n",
       "_y, C_z)) + Txz(C_x, C_y, C_z)⋅────(vx(C_x, C_y, C_z))\n",
       "                               ∂C_z                   "
      ]
     },
     "execution_count": 286,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T.row(0).dot(gradient(v.dot(C.i),doit=True).to_matrix(C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 287,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{Tyx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Tyy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Tyz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "                    ∂                                            ∂            \n",
       "Tyx(C_x, C_y, C_z)⋅────(vy(C_x, C_y, C_z)) + Tyy(C_x, C_y, C_z)⋅────(vy(C_x, C\n",
       "                   ∂C_x                                         ∂C_y          \n",
       "\n",
       "                                ∂                     \n",
       "_y, C_z)) + Tyz(C_x, C_y, C_z)⋅────(vy(C_x, C_y, C_z))\n",
       "                               ∂C_z                   "
      ]
     },
     "execution_count": 287,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T.row(1).dot(gradient(v.dot(C.j),doit=True).to_matrix(C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{Tyx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Tyy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Tyz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "                    ∂                                            ∂            \n",
       "Tyx(C_x, C_y, C_z)⋅────(vy(C_x, C_y, C_z)) + Tyy(C_x, C_y, C_z)⋅────(vy(C_x, C\n",
       "                   ∂C_x                                         ∂C_y          \n",
       "\n",
       "                                ∂                     \n",
       "_y, C_z)) + Tyz(C_x, C_y, C_z)⋅────(vy(C_x, C_y, C_z))\n",
       "                               ∂C_z                   "
      ]
     },
     "execution_count": 285,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T.row(1).dot(gradient(v.dot(C.j),doit=True).to_matrix(C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 288,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/latex": [
       "$\\displaystyle \\operatorname{Txx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Txy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + \\operatorname{Txz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + 2 \\operatorname{Tyx}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{x}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + 2 \\operatorname{Tyy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{y}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} + 2 \\operatorname{Tyz}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)} \\frac{\\partial}{\\partial \\mathbf{{z}_{C}}} \\operatorname{vy}{\\left(\\mathbf{{x}_{C}},\\mathbf{{y}_{C}},\\mathbf{{z}_{C}} \\right)}$"
      ],
      "text/plain": [
       "                    ∂                                            ∂            \n",
       "Txx(C_x, C_y, C_z)⋅────(vx(C_x, C_y, C_z)) + Txy(C_x, C_y, C_z)⋅────(vx(C_x, C\n",
       "                   ∂C_x                                         ∂C_y          \n",
       "\n",
       "                                ∂                                             \n",
       "_y, C_z)) + Txz(C_x, C_y, C_z)⋅────(vx(C_x, C_y, C_z)) + 2⋅Tyx(C_x, C_y, C_z)⋅\n",
       "                               ∂C_z                                           \n",
       "\n",
       " ∂                                              ∂                             \n",
       "────(vy(C_x, C_y, C_z)) + 2⋅Tyy(C_x, C_y, C_z)⋅────(vy(C_x, C_y, C_z)) + 2⋅Tyz\n",
       "∂C_x                                           ∂C_y                           \n",
       "\n",
       "                 ∂                     \n",
       "(C_x, C_y, C_z)⋅────(vy(C_x, C_y, C_z))\n",
       "                ∂C_z                   "
      ]
     },
     "execution_count": 288,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T.row(0).dot(gradient(v.dot(C.i),doit=True).to_matrix(C)) + T.row(1).dot(gradient(v.dot(C.j),doit=True).to_matrix(C)) + T.row(1).dot(gradient(v.dot(C.j),doit=True).to_matrix(C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
