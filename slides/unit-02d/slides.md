# MME 3303A: Fluid Mechanics  
## Unit 2: Differential Relations for Fluid Flow
## Topic 4: Exact Solutions
Instructor: C.T. DeGroot, PhD, PEng  

---
<!-- Section 01: Unit Learning Objectives-->
## Topic Learning Objectives

- Be able to solve the governing equations of fluid mechanics for selected scenarios where an exact solution exists.

---
<!-- Section 02: Steady, Laminar Flow Between Fixed Infinite Parallel Plates-->
<!-- .slide: class="student-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

- Consider steady, laminar flow where the fluid is moving on one direction only.

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

- Consider steady, laminar flow where the fluid is moving on one direction only.

>- Draw diagram of the flow, with x-direction in the direction of the flow; Channel height is $2h$, with $y=0$ in the middle of the channel.
>- Note that $v=0$ and $w=0$.
>- Invoke continuity for incompressible flow to get $\frac{\partial u}{\partial x} = 0$, such that $u = u(y, z)$.
>- But, if the plates are infinite, $u$ does not depends on z, so $u = u(y)$.
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

>- z-momentum shows that $\frac{\partial p}{\partial z} = 0$
>- Now, invoke y-momentum:
>- $ \rho \left( \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} \right) = \rho g_y - \frac{\partial p}{\partial y} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} + \frac{\partial^2 v}{\partial z^2}\right) $
>- Cancel everything except pressure and gravity term.
>- $ \frac{\partial p}{\partial y} = - \rho g $
>- $ p = - \rho g (y - y_0) $ (hydrostatic pressure variation)
>- But, if the channel dimension is not too large, we can ignore this
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

>- Now, x-momentum:
>- $ \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right) = \rho g_x - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}\right) $
>- Results in:
>- $ 0 = \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial y^2} \right) $
>- If we ignore pressure variation in y, $\frac{\partial p}{\partial x} \rightarrow \frac{dp}{dx}$
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

>- For $u=u(y)$ (i.e., not a function of x), $\frac{dp}{dx}$ must be constant
>- Integrate x-momentum:
>- $ \frac{\partial^2 u}{\partial y^2} = \frac{1}{\mu} \frac{dp}{dx} $
>- $ \frac{\partial u}{\partial y} = \frac{1}{\mu} \frac{dp}{dx} y + c_1 $
>- $ u(y) = \frac{1}{2 \mu} \frac{dp}{dx} y^2 + c_1 y + c_2 $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

>- Find the constants using boundary conditions:
>- $ u(-h) = 0 = \frac{1}{2 \mu} \frac{dp}{dx} h^2 - c_1 h + c_2 $
>- $ u(h) = 0 = \frac{1}{2 \mu} \frac{dp}{dx} h^2 + c_1 h + c_2 $
>- Add equations:
>- $ 0 = \frac{1}{\mu} \frac{dp}{dx} h^2 + 2 c_2  \rightarrow c_2 = - \frac{1}{2 \mu} \frac{dp}{dx} h^2 $
>- Subtract equations:
>- $ 0 = 2 c_1 \rightarrow c_1 = 0 $ 
>- $ u(y) = \frac{1}{2 \mu} \frac{dp}{dx} ( y^2 - h^2) $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case I: Steady, Laminar Flow Between Fixed Infinite Parallel Plates

>- $ \frac{dp}{dx} $ must be negative to drive flow in positive x-direction,
>- The velocity profile is parabolic (draw it),
>- The volume flow rate, per unit width, is:
>- $ q = \int_{-h}^{h} u dy = \int_{-h}^{h} \frac{1}{2 \mu} \frac{dp}{dx} ( y^2 - h^2) dy $
>- $ q = \frac{1}{2 \mu} \frac{dp}{dx} \left[ \frac{y^3}{3} - h^2 y \right]^h_{-h} = \frac{1}{2 \mu} \frac{dp}{dx} \left[ \left( \frac{h^3}{3} - h^3 \right) - \left( - \frac{h^3}{3} + h^3 \right) \right] $
>- $ q = \frac{1}{2 \mu} \frac{dp}{dx} \left( \frac{2h^3}{3} - 2h^3 \right) = -\frac{2}{3} \frac{h^3}{\mu} \frac{dp}{dx}$
<!-- .element: class="annotation-space" -->

---
<!-- Section 03: Liquid Film Flowing Down an Infinite Vertical Plate-->
<!-- .slide: class="student-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

- Consider steady, incompressible, laminar flow of a liquid film flowing down an infinite vertical plate under the action of gravity:

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

- Consider steady, incompressible, laminar flow of a liquid film flowing down an infinite vertical plate under the action of gravity:

>- Draw a vertical plate with y in the upward direction, x in the right direction, and z out of the page. The liquid film has constant thickness h. Gravity is down.
>- Since plate is infinite in the z-direction $\frac{\partial}{\partial z} = 0$
>- Assume no u velocity,
>- Continuity gives $\frac{\partial v}{\partial y} = 0$, so $v = v(x)$,
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

>- $g_x = 0$, $g_y = g$, $g_z = 0$
>- $ \rho \left( \cancel{\frac{\partial u}{\partial t}} + \cancel{u \frac{\partial u}{\partial x}} + \cancel{v \frac{\partial u}{\partial y}} + \cancel{w \frac{\partial u}{\partial z}} \right) = \cancel{\rho g_x} - \frac{\partial p}{\partial x} + \mu \left( \cancel{\frac{\partial^2 u}{\partial x^2}} + \cancel{\frac{\partial^2 u}{\partial y^2}} + \cancel{\frac{\partial^2 u}{\partial z^2}} \right) $
>- $ \frac{\partial p}{\partial x} = 0 $
>- $ \rho \left( \cancel{\frac{\partial v}{\partial t}} + \cancel{u} \frac{\partial v}{\partial x} + v \cancel{\frac{\partial v}{\partial y}} + \cancel{w \frac{\partial v}{\partial z}} \right) = \rho g - \cancel{\frac{\partial p}{\partial y}} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \cancel{\frac{\partial^2 v}{\partial y^2}} + \cancel{\frac{\partial^2 v}{\partial z^2}} \right) $
>- Flow is gravity driven so no pressure gradient.
>- $ \frac{\partial^2 v}{\partial x^2} = \frac{\rho g}{\mu} $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

>- $ \frac{d^2 v}{d x^2} = \frac{\rho g}{\mu} $
>- $ \frac{dv}{dx} = \frac{\rho g}{\mu}x + c_1 $
>- $ v(x) = \frac{\rho g}{2 \mu}x^2 + c_1 x + c_2 $
>- Boundary conditions: (i) no slip at $x=0$ and zero shear at $x=h$
>- $ \tau_{xy} = \mu \left( \cancel{\frac{\partial u}{\partial y}} + \frac{\partial v}{\partial x} \right) = 0$
>- $ \left. \frac{dv}{dx} \right|_{x=h} = 0 $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case II: Liquid Film Flowing Down an Infinite Vertical Plate

>- $ v(x=0) = c_2 = 0 $
>- $ \frac{dv}{dx} = \frac{\rho g}{\mu}x + c_1$
>- $ \left. \frac{dv}{dx} \right|_{x=h} =  \frac{\rho g}{\mu}h + c_1 = 0 $
>- $ c_1 = - \frac{\rho g h}{\mu} $
>- $ v(x) = \frac{\rho g}{2 \mu}x^2 - \frac{\rho g h}{\mu} x $
>- $ v(x) = \frac{\rho g h^2}{2 \mu} \left[ \left( \frac{x}{h} \right)^2 - 2 \frac{x}{h}  \right] $
<!-- .element: class="annotation-space" -->

---
<!-- Section 04: Poiseuille Flow -->
<!-- .slide: class="student-only" -->
## Case III: Poiseuille Flow

- Steady, incompressible, laminar flow in straight, horizontal circular pipe (this flow is known as *Poiseuille Flow*):

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case III: Poiseuille Flow

- Steady, incompressible, laminar flow in straight, horizontal circular pipe (this flow is known as *Poiseuille Flow*):

>- Draw a pipe and note that it is convenient to use cylindrical coordinates. Draw z along the axis, r pointing to the outer part of the circle, and $\theta$ from a reference axis. The outer radius is $R$. 
>- Flow is entirely in the z-direction so $v_r = 0$ and $v_\theta = 0$.
>- Additionally, it is axisymmetric, so $\frac{\partial}{\partial \theta} = 0$.
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case III: Poiseuille Flow

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case III: Poiseuille Flow

>- Incompressible continuity equation in cylindrical coordinates:
>- $ \frac{1}{r} \frac{\partial (r \cancel{u_r})}{\partial r} + \frac{1}{r} \cancel{\frac{\partial u_\theta}{\partial \theta}} + \frac{\partial u_z}{\partial z} = 0 $
>- $ \frac{\partial v_z}{\partial z} = 0 $
>- Shows that the flow is *fully developed* in the z-direction.
>- $ u_z = u_z(r) $
>- Draw cross-section of pipe where $\theta$ is measured counter-clockwise from the axis pointing the right of centre to the $r$ vector. Draw gravity vector down.
>- $g_r = -g\sin\theta$, $g_\theta = -g \cos\theta$, $g_z = 0$.
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case III: Poiseuille Flow

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case III: Poiseuille Flow

>- $r$ momentum equation:
>- $ \rho \left( \frac{\partial u_r}{\partial t} + u_r \frac{\partial u_r}{\partial r} + \frac{u_\theta}{r} \frac{\partial u_r} {\partial \theta} + u_z \frac{\partial u_r}{\partial z} - \frac{u_\theta^2}{r} \right) = \rho g_r - \frac{\partial p}{\partial r} \quad\quad $
$ \quad\quad + \mu \left[ \frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial u_r}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u_r}{\partial \theta^2} + \frac{\partial^2 u_r}{\partial z^2} - \frac{u_r}{r^2} - \frac{2}{r^2}\frac{\partial u_\theta}{\partial \theta} \right] $
>- $ 0 = -\rho g\sin\theta - \frac{\partial p}{\partial r} $
>- $ p = -\rho g r \sin\theta + c_1(z, \theta) $
>- $\theta$ momentum equation:
>- $ \rho \left( \frac{\partial u_\theta}{\partial t} + u_r \frac{\partial u_\theta}{\partial r} + \frac{u_\theta}{r} \frac{\partial u_\theta}{\partial \theta} + u_z \frac{\partial u_\theta}{\partial z} + \frac{u_r u_\theta}{r} \right) = \rho g_\theta - \frac{1}{r}\frac{\partial p}{\partial \theta} \quad\quad$
$ \quad\quad \mu \left[\frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial u_\theta}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u_\theta}{\partial \theta^2} + \frac{\partial^2 u_\theta}{\partial z^2} - \frac{u_\theta}{r^2} + \frac{2}{r^2}\frac{\partial u_r}{\partial \theta} \right] $
>- $ 0 = -\rho g\cos\theta - \frac{1}{r}\frac{\partial p}{\partial \theta} $
>- $ p = -\rho g r \sin\theta + c_2(z, r) $
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case III: Poiseuille Flow

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case III: Poiseuille Flow

>- Compare the two equations for pressure:
>- $ p = -\rho g r \sin\theta + c_1(z, \theta) $
>- $ p = -\rho g r \sin\theta + c_2(z, r) $
>- To be consistent, $c_1(z, \theta)$ must equal $c_2(z, r)$. For this to be the case, it can only be a function of z, so:
>- $c_1(z, \theta) = c_2(z, r) = c(z) $
>- Therefore $ p = -\rho g r \sin\theta + c(z) $
>- Note that $ y = r\sin\theta $ so this describes a hydrostatic pressure variation.
>- Since $ u_z $ does not change with $z$ we can assume $\frac{\partial p}{\partial z} = \text{const}$
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case III: Poiseuille Flow

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case III: Poiseuille Flow

>- $z$ momentum equation:
>- $ \rho \left( \frac{\partial u_z}{\partial t} + u_r \frac{\partial u_z}{\partial r} + \frac{u_\theta}{r} \frac{\partial u_z}{\partial \theta} + u_z \frac{\partial u_z}{\partial z} \right)
= \rho g_z - \frac{\partial p}{\partial z} + \mu \left[ \frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial u_z}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u_z}{\partial \theta^2} + \frac{\partial^2 u_z}{\partial z^2} \right] $
>- $ 0 = - \frac{\partial p}{\partial z} + \mu \left[ \frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial u_z}{\partial r}\right) \right] $
>- $ \frac{\partial}{\partial r}\left(r \frac{\partial u_z}{\partial r}\right) = \frac{1}{\mu}\frac{\partial p}{\partial z} r $
>- $r \frac{\partial u_z}{\partial r} = \frac{1}{2\mu} \frac{\partial p}{\partial z} r^2 + c_1 $
>- $ \frac{\partial u_z}{\partial r} = \frac{1}{2\mu} \frac{\partial p}{\partial z} r + \frac{c_1}{r} $
>- $ u_z = \frac{1}{4\mu} \frac{\partial p}{\partial z} r^2 + c_1\ln(r) +c_2 $
>- Since $\ln(0) \rightarrow \infty$, $c_1 = 0$ so that the velocity is finite at $r=0$
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case III: Poiseuille Flow

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case III: Poiseuille Flow

>- Apply no-slip condition at $r=R$:
>- $ u_z = \frac{1}{4\mu} \frac{\partial p}{\partial z} R^2 + c_2 = 0$
>- $ c_2 = -\frac{1}{4\mu} \frac{\partial p}{\partial z} R^2 $
>- $ u_z(r) = \frac{1}{4\mu} \frac{\partial p}{\partial z} \left( r^2 - R^2 \right) $
>- Profile is parabolic (draw it).
>- $ u_{max} = u(r=0) = - \frac{R^2}{4\mu} \frac{\partial p}{\partial z} $
>- Note pressure gradient is negative.
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## Case III: Poiseuille Flow

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Case III: Poiseuille Flow

>- Calculate volume flow rate:
>- $ q = \int_0^R u_z dA = \int_0^R u_z (2\pi r) dr $
>- $ q = 2\pi \int_0^R \left[ \frac{1}{4\mu} \frac{\partial p}{\partial z} \left( r^2 - R^2 \right) \right]  r dr $
>- $ q = \frac{\pi}{2\mu} \frac{\partial p}{\partial z} \int_0^R \left( r^3 - rR^2 \right) dr $
>- $ q = \frac{\pi}{2\mu} \frac{\partial p}{\partial z} \left[ \frac{r^4}{4} - \frac{r^2R^2}{2} \right]^R_0 $
>- $ q = \frac{\pi}{2\mu} \frac{\partial p}{\partial z} \left[ \frac{R^4}{4} - \frac{R^4}{2} \right] $
>- $ q = - \frac{\pi R^4}{8\mu} \frac{\partial p}{\partial z} $
<!-- .element: class="annotation-space" -->