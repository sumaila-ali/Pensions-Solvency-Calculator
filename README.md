📘 Pension System Formula Documentation

📈 Contributors

term₁ = (ε₁ / (λ₁ - μ₁)) · e^((λ₁ - μ₁)t)

term₂ = init_pop_cont · e^((λ₁ - μ₁)t)

entire_pop_cont = ∫ (term₁ + term₂) dt

total_cont = entire_pop_cont · Ave_cont



⸻

💰 Lump Sum Recipients

lump_pop₁ = init_lump_pop₁ · (1 - e^(−μ₂·t))

lump_pop₂ = init_lump_pop₂ · (1 - e^(−ε₂·t))

total_lump = lump_pop₁ · Ave_lump₁ + lump_pop₂ · Ave_lump₂



⸻

🧓 Pension Recipients

term₃ = (ε₂ / (λ₂ - μ₂)) · e^((λ₂ - μ₂)t)

term₄ = init_pen_pop · e^((λ₂ - μ₂)t)

pen_pop = ∫ (term₃ + term₄) dt

total_pen = pen_pop · Ave_pen



⸻

📌 Variables

Symbol	Description

ε₁, ε₂	Entry rates into contributors/pension

λ₁, λ₂	Contributor and pensioner growth rates

μ₁, μ₂	Contributor and pensioner exit/death rates

init_*	Initial population in each category

Ave_*	Average contribution or payout

t	Time (years)



⸻
