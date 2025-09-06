# MME 3303A: Fluid Mechanics  
## Unit 2: Differential Relations for Fluid Flow
## Topic 1: Overview and Mathematical Foundations
Instructor: C.T. DeGroot, PhD, PEng  

---
<!-- Section 01: Unit Learning Objectives-->
## Topic Learning Objectives

- Be able to apply fundamental mathematical concepts including unit vectors, chain rule, Taylor series, and gradient/divergence operators.
- Be able to derive the acceleration vector for a fluid in motion.

---
<!-- Section 02: Integral vs. Differential Analysis-->
## Integral vs. Differential Analysis

- We introduced this briefly in Unit 1.

--
## Integral Approach

- Integral approach:
    - Estimate overall behaviour over a defined control volume.
    - Cannot get detailed information about behaviour inside the control volume.
    - Useful for modelling system behaviour but cannot understand or optimize device performance.

--
## Differential Approach

- Differential approach:
    - Basic conservation laws are applied over infinitesimally small control volumes, defining the governing differential equations for the fluid motion.
    - Can obtain velocity for any point within the region of interest when the equations can be solved analytically.
    - This is also the approach underlying any numerical simulation software.
    - Differential analysis is necessary to understand or improve device performance.

---
<!-- Section 03: Mathematical Fundamentals-->
## Mathematical Fundamentals

- In this section, we will:
    - Review unit vectors.
    - Review the chain rule of calculus.
    - Review Taylor series.
    - Define useful mathematical operators.

--
## Unit Vectors

- A **unit vector** always has a magnitude of 1 and points in a specific direction.
- Denoted with a "hat": e.g., $\hat{\mathbf{i}}$, $\hat{\mathbf{j}}$, $\hat{\mathbf{k}}$.
- In Cartesian coordinates:
  - $\hat{\mathbf{i}} = (1, 0, 0)$
  - $\hat{\mathbf{j}} = (0, 1, 0)$
  - $\hat{\mathbf{k}} = (0, 0, 1)$

--
<!-- .slide: class="student-only" -->
## The Chain Rule of Calculus

- The chain rule tells us how to differentiate a function of a composition of functions, e.g.:

<div class="annotation-space"></div>

--
<!-- .slide: class="instructor-only" -->
## The Chain Rule of Calculus

- The chain rule tells us how to differentiate a function of a composition of functions, e.g.:

>- $ z = z(y) $ (z is a function of y)
>- $ y = y(x) $ (y is a function of x)
>- $ z = z(x, y) $ (z must be a function of both x and y)
>- $ \frac{dz}{dx} = \frac{dz}{dy}\frac{dy}{dz} $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## The Chain Rule Example 1

- Example: If $z = y^2$ and $y = 2x + 1$, find $ \frac{dz}{dx}$.

<div class="annotation-space annotation-h-50"></div>

--
<!-- .slide: class="instructor-only" -->
## The Chain Rule Example 1

- Example: If $z = y^2$ and $y = 2x + 1$, find $ \frac{dz}{dx}$.

>- $ \frac{dz}{dy} = 2y $ 
>- $ \frac{dy}{dx} = 2 $ 
>- $ \frac{dz}{dx} = \frac{dz}{dy}\frac{dy}{dz} = 4y $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## The Chain Rule Example 2

- Example: If $z = x^2 + y^2$, $y = 2t$, and $z = 5t$ find $ \frac{dz}{dt}$.

<div class="annotation-space annotation-h-50"></div>

--
<!-- .slide: class="instructor-only" -->
## The Chain Rule Example 2

- Example: If $z = x^2 + y^2$, $y = 2t$, and $z = 5t$ find $ \frac{dz}{dt}$.

>- $ \frac{\partial z}{\partial x} = 2x $ (note it is a partial derivative!)
>- $ \frac{\partial z}{\partial y} = 2y $ 
>- $ \frac{dx}{dt} = 5 $
>- $ \frac{dy}{dt} = 2 $
>- $ \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} $
>- $ \frac{dz}{dt} = 2x\cdot 5 + 2y\cdot 2 = 10x + 4y$
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Taylor Series

- Taylor series are used to approximate a function based on its value and derivatives at a single point:

<div class="annotation-space annotation-h-50"></div>

--
<!-- .slide: class="instructor-only" -->
## Taylor Series

- Taylor series are used to approximate a function based on its value and derivatives at a single point:

>- $ f(x) = f(a) + \frac{f^\prime(a)}{1!}(x - a) + \frac{f^\prime(a)}{2!}(x - a)^2 + \ldots + \frac{f^{(n)}(a)}{n!}(x - a)^n $
>- $ f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x - a)^n $
>- Draw a function and show how it would be approximated with just the first derivative
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Useful Operators

- Gradient and divergence operators are commonly used in fluid mechanics:

<div class="annotation-space annotation-h-50"></div>

--
<!-- .slide: class="instructor-only" -->
## Useful Operators

- Gradient and divergence operators are commonly used in fluid mechanics:

>- $ grad(f) = \nabla f = \frac{\partial f}{\partial x} \hat{i} + \frac{\partial f}{\partial y} \hat{j} + \frac{\partial f}{\partial z} \hat{k} $
>- From this we can say: $ \nabla = \frac{\partial}{\partial x} \hat{i} + \frac{\partial}{\partial y} \hat{j} + \frac{\partial}{\partial z} \hat{k}$
>- $ div(f) = \nabla\cdot\vec{f} $
>- $ div(f) = \left( \frac{\partial}{\partial x} \hat{i} + \frac{\partial}{\partial y} \hat{j} + \frac{\partial}{\partial z} \hat{k} \right)\cdot \left(f_x\hat{i} + f_y\hat{j} + f_z\hat{k} \right)  $
>- $ div(f) = \frac{\partial f_x}{\partial x} + \frac{\partial f_y}{\partial y} + \frac{\partial f_z}{\partial z} $
<!-- .element: class="annotation-space" -->

---
<!-- Section 04: Acceleration of a Fluid-->
## Acceleration of a Fluid

- In this section, we will:
    - Define the fluid velocity vector.
    - Define the acceleration of a fluid.

--
<!-- .slide: class="student-only" -->
## The Fluid Velocity Vector

- The fluid velocity vector varies in space and time.
- Using the Cartesian unit vectors, the velocity is expressed as:

<div class="annotation-space annotation-h-30"></div>

- $u$, $v$, $w$ are $f(x, y, z, t)$.
- "Solving" a fluid mechanics problem essentially means finding the velocity field.

--
<!-- .slide: class="instructor-only" -->
## The Fluid Velocity Vector

- The fluid velocity vector varies in space and time.
- Using the Cartesian unit vectors, the velocity is expressed as:

> $ \vec{v} = u\hat{i} + v\hat{j} + w\hat{k} $
> - Draw a 2D vector and show the components
<!-- .element: class="annotation-space" -->

- $u$, $v$, $w$ are $f(x, y, z, t)$.
- "Solving" a fluid mechanics problem essentially means finding the velocity field.

--
## Acceleration of a Fluid

- The basic definition of the fluid acceleration at a point in space and time is:

$$ \vec{a} = \frac{d\vec{v}}{dt} = \frac{du}{dt}\hat{i} + \frac{dv}{dt}\hat{j} + \frac{dw}{dt}\hat{k} $$

- However: u = u(x, y, z, t), v = v(x, y, z, t), w = w(x, y, z, t).
- Therefore we must apply chain rule.

--
<!-- .slide: class="student-only" -->
## Acceleration in x-Direction

- First, find $ \frac{du}{dt}$ where u(x, y, z, t):

<div class="annotation-space annotation-h-50"></div>

--
<!-- .slide: class="instructor-only" -->
## Acceleration in x-Direction

- First, find $ \frac{du}{dt}$ where u(x, y, z, t):

>- $ \frac{du}{dt} = \frac{\partial u}{\partial t}\frac{dt}{dt} + \frac{\partial u}{\partial x}\frac{dx}{dt} + \frac{\partial u}{\partial y}\frac{dy}{dt}+ \frac{\partial u}{\partial z}\frac{dz}{dt} $
>- $ \frac{du}{dt} = \frac{\partial u}{\partial t} + \frac{\partial u}{\partial x}\frac{dx}{dt} + \frac{\partial u}{\partial y}\frac{dy}{dt}+ \frac{\partial u}{\partial z}\frac{dz}{dt} $ 
> - By definition $ u = \frac{dx}{dt} $, $ v = \frac{dy}{dt} $, $ w = \frac{dz}{dt} $
>- $ a_x = \frac{du}{dt} = \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} $
>- Applying the gradient operator:
>- $ a_x = \frac{\partial u}{\partial t} + (\vec{v}\cdot\nabla) u $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Acceleration in y- and z-Directions

- Next, find $a_y$ and $a_z$:

<div class="annotation-space annotation-h-50"></div>

--
<!-- .slide: class="instructor-only" -->
## Acceleration in y- and z-Directions

- Next, find $a_y$ and $a_z$:

>- $ a_y = \frac{dv}{dt} = \frac{\partial v}{\partial t} + (\vec{v}\cdot\nabla) v $
>- $ a_z = \frac{dw}{dt} = \frac{\partial w}{\partial t} + (\vec{v}\cdot\nabla) w $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Acceleration Vector

- Now, combine to form the acceleration vector:

<div class="annotation-space annotation-h-50"></div>

--
<!-- .slide: class="instructor-only" -->
## Acceleration Vector

- Now, combine to form the acceleration vector:

>- $ \vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k} $
>- $ \vec{a} = \frac{\partial\vec{v}}{\partial t} + (\vec{v}\cdot\nabla)\vec{v} $
>- $ \vec{a} = \frac{\partial\vec{v}}{\partial t} + \left( u \frac{\partial\vec{v}}{\partial x} + v \frac{\partial\vec{v}}{\partial y} + w \frac{\partial\vec{v}}{\partial z} \right) $
>- $ \frac{\partial\vec{v}}{\partial t} $ is the local acceleration
>- $ (\vec{v}\cdot\nabla)\vec{v} $ is the convective acceleration
<!-- .element: class="annotation-space" -->

--
## Acceleration Components

- The local acceleration, $\frac{\partial\vec{v}}{\partial t}$:
    - Represents acceleration due to change in velocity over time for a fluid parcel.
    - For steady flow is zero.
- The convective acceleration, $(\vec{v}\cdot\nabla)\vec{v}$:
    - Arises when fluid parcel moves through regions of varying velocity.
    - Can be non-zero in both steady and unsteady flows.

--
<!-- .slide: class="student-only" -->
## Total Derivative

- We can also define the "total derivative", $ \frac{D}{Dt} $, as:

<div class="annotation-space annotation-h-30"></div>

- It is also sometimes called the "material derivative" or "substantial derivative".

--
<!-- .slide: class="instructor-only" -->
## Total Derivative

- We can also define the "total derivative", $ \frac{D}{Dt} $, as:

>- $ \frac{D}{Dt} = \frac{\partial}{\partial t} + \left( u \frac{\partial}{\partial x} + v \frac{\partial}{\partial y} + w \frac{\partial}{\partial z} \right)  $
>- So that:
>- $ \vec{a} = \frac{D\vec{v}}{Dt} = \frac{\partial\vec{v}}{\partial t} + \left( u \frac{\partial\vec{v}}{\partial x} + v \frac{\partial\vec{v}}{\partial y} + w \frac{\partial\vec{v}}{\partial z} \right) $
<!-- .element: class="annotation-space" -->

- It is also sometimes called the "material derivative" or "substantial derivative".