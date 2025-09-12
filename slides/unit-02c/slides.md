# MME 3303A: Fluid Mechanics  
## Unit 2: Differential Relations for Fluid Flow
## Topic 3: Navier-Stokes Equations
Instructor: C.T. DeGroot, PhD, PEng  

---
<!-- Section 01: Unit Learning Objectives-->
## Topic Learning Objectives

- Be able to define the shear stress in terms of the velocity gradient for Newtonian fluids.
- Understand the applicability and limitations of the Navier-Stokes equations.
- Be able to identify appropriate boundary conditions for the Navier-Stokes equations.

---
<!-- Section 02: Viscous Flows-->
## Viscous Flows

- *Viscous flows* are ones where the viscous effects are significant and cannot be ignored when seeking a solution.
- *Inviscid flows* are ones where viscous effects can be ignored.
    - All shear stress components are set to zero.
    - The normal stress is equal to the pressure only.
- By defining a relationship between stresses (normal and shear) and velocity we can reduce the number of unknowns.

-- 
<!-- .slide: class="student-only" -->
## Viscous Stresses

- For Newtonian fluids, the viscous stresses are:

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Viscous Stresses

- For Newtonian fluids, the viscous stresses are:

>- $ \tau_{xx} = 2\mu \frac{\partial u}{\partial x}$, $ \tau_{yy} = 2\mu \frac{\partial v}{\partial y}$, $ \tau_{zz} = 2\mu \frac{\partial w}{\partial z}$
>- $ \tau_{xy} = \tau_{yz} = \mu \left( \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x} \right) $
>- $ \tau_{xz} = \tau_{zx} = \mu \left( \frac{\partial w}{\partial x} + \frac{\partial u}{\partial z} \right) $
>- $ \tau_{yz} = \tau_{zy} = \mu \left( \frac{\partial v}{\partial z} + \frac{\partial w}{\partial y} \right) $
<!-- .element: class="annotation-space" -->

-- 
<!-- .slide: class="student-only" -->
## Normal Stresses

- The normal stresses have both a viscous and pressure component:

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## Normal Stresses

- The normal stresses have both a viscous and pressure component:

>- $ \sigma_{xx} = -p + \tau_{xx} $
>- $ \sigma_{yy} = -p + \tau_{yy} $
>- $ \sigma_{zz} = -p + \tau_{zz} $
<!-- .element: class="annotation-space" -->

---
<!-- Section 03: Navier-Stokes Equations-->
<!-- .slide: class="student-only" -->
## The Navier-Stokes Equations

- Substitute the stress components into the general momentum equations and assume constant density to derive the Navier-Stokes equations:

<div class="annotation-space"></div>

-- 
<!-- .slide: class="instructor-only" -->
## The Navier-Stokes Equations

- Substitute the stress components into the general momentum equations and assume constant density to derive the Navier-Stokes equations:

$ \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right) = \rho g_x - \frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}\right) $
$ \rho \left( \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} \right) = \rho g_y - \frac{\partial p}{\partial y} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} + \frac{\partial^2 v}{\partial z^2}\right) $
$ \rho \left( \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} \right) = \rho g_z - \frac{\partial p}{\partial z} + \mu \left( \frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial y^2} + \frac{\partial^2 w}{\partial z^2}\right) $
$ \rho \left[ \frac{\partial \vec{v}}{\partial t} + (\vec{v}\cdot\nabla)\vec{v} \right] = \rho \vec{g} - \nabla p + \mu \nabla^2\vec{v} $
<!-- .element: class="annotation-space" -->

--
## Navier-Stokes Equations in Cylindrical Coordinates

$$ \rho \left( \frac{\partial u_r}{\partial t} + u_r \frac{\partial u_r}{\partial r} + \frac{u_\theta}{r} \frac{\partial u_r} {\partial \theta} + u_z \frac{\partial u_r}{\partial z} - \frac{u_\theta^2}{r} \right) = \rho g_r - \frac{\partial p}{\partial r} \quad\quad $$
$$ \quad\quad + \mu \left[ \frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial u_r}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u_r}{\partial \theta^2} + \frac{\partial^2 u_r}{\partial z^2} - \frac{u_r}{r^2} - \frac{2}{r^2}\frac{\partial u_\theta}{\partial \theta} \right] $$

$$ \rho \left( \frac{\partial u_\theta}{\partial t} + u_r \frac{\partial u_\theta}{\partial r} + \frac{u_\theta}{r} \frac{\partial u_\theta}{\partial \theta} + u_z \frac{\partial u_\theta}{\partial z} + \frac{u_r u_\theta}{r} \right) = \rho g_\theta - \frac{1}{r}\frac{\partial p}{\partial \theta} \quad\quad$$
$$ \quad\quad \mu \left[\frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial u_\theta}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u_\theta}{\partial \theta^2} + \frac{\partial^2 u_\theta}{\partial z^2} - \frac{u_\theta}{r^2} + \frac{2}{r^2}\frac{\partial u_r}{\partial \theta} \right] $$

$$ \rho \left( \frac{\partial u_z}{\partial t} + u_r \frac{\partial u_z}{\partial r} + \frac{u_\theta}{r} \frac{\partial u_z}{\partial \theta} + u_z \frac{\partial u_z}{\partial z} \right)
= \rho g_z - \frac{\partial p}{\partial z} + \mu \left[ \frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial u_z}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u_z}{\partial \theta^2} + \frac{\partial^2 u_z}{\partial z^2} \right] $$

--
## Comments on Navier-Stokes Equations

- Main assumptions:
    - Incompressible.
    - Newtonian fluid (with constant viscosity).
- Combined with continuity equation, these give a complete mathematical description of the flow.
    - Unknowns: u, v, w, p.
    - We have 4 equations for 4 unknowns.
- In reality, the equations are very hard to solve except for a few special cases.

--
## Solution of Navier-Stokes Equations

- No general solutions exist.
- For most practical flow problems, the convective acceleration is important.
    - These terms are non-linear, and make solution difficult.
    - In some special cases, these terms vanish and an exact solution can be found.
- Technically, the equations are valid for laminar and turbulent flows.
    - Turbulent flows are always transient and the convective term is important, so there are no exact solutions.

---
<!-- Section 04: Initial and Boundary Conditions-->
## Initial and Boundary Conditions

- To solve the N-S equations, boundary conditions are required.
- For transient problems, initial conditions are also required.
- The initial and boundary conditions are what define the particular flow problem being analyzed. 
- For viscous flows, the most common boundary conditions are the *no-slip* and *no-penetration* conditions.

--
<!-- .slide: class="student-only" -->
## No-Slip Boundary Condition

- In all real flows, the fluid immediately adjacent to the solid surface does not move relative to that surface.
    - The fluid "sticks" to the surface.
- The no-slip condition states that the tangential component of the fluid velocity at the bounding surface must be equal to the tangential velocity of the bounding surface.

<div class="annotation-space"></div>

--
<!-- .slide: class="instructor-only" -->
## No-Slip Boundary Condition

- In all real flows, the fluid immediately adjacent to the solid surface does not move relative to that surface.
    - The fluid "sticks" to the surface.
- The no-slip condition states that the tangential component of the fluid velocity at the bounding surface must be equal to the tangential velocity of the bounding surface.

>- Draw moving surface (e.g., fan blade) and stationary surface (e.g., pipe) and label velocity.
<!-- .element: class="annotation-space" -->

--
<!-- .slide: class="student-only" -->
## No-Penetration Boundary Condition

- The no-penetration condition arises because the fluid cannot penetrate an impermeable bounding surface.
- This condition requires that the normal component of the fluid velocity must be equal to the normal velocity of the bounding surface.

<div class="annotation-space"></div>

--
<!-- .slide: class="instructor-only" -->
## No-Penetration Boundary Condition

- The no-penetration condition arises because the fluid cannot penetrate an impermeable bounding surface.
- This condition requires that the normal component of the fluid velocity must be equal to the normal velocity of the bounding surface.

>- Draw moving surface (e.g., fan blade) and stationary surface (e.g., pipe) and label velocity.
<!-- .element: class="annotation-space" -->