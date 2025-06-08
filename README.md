📘 Pension System Formula Documentation

📈 Contributors

(ε₁ / (λ₁ - μ₁)) · e^((λ₁ - μ₁)t):
Populations of joiners to the scheme influenced by external factors like a change in government policy. 


initialContributorPopulation · e^((λ₁ - μ₁)t):
Population of joiners to the scheme influenced by the internal factors like the joining rate of new contributors(λ₁) and drop off rate of contributors(μ₁). 

∫ (term₁ + term₂) dt: 
Population of contributors. 


⸻

💰 Lump Sum Recipients

initialLumpSumRecipients · (1 - e^(−μ₂·t)):
Modeling the growth of the population of members who will be recieving their first lump sum over time. 
ie: members who just retired. 

finalLumpSumRecipients· (1 - e^(−ε₂·t)):
Modeling the growth of the population of members who will be recieving their last lump sum over time. 
ie: members who just died. 


⸻

🧓 Pension Recipients

(ε₂ / (λ₂ - μ₂)) · e^((λ₂ - μ₂)t): 
Populations of pensioners in the scheme influenced by external factors like a change in retirement age. 



initialAnnuityRecipients · e^((λ₂ - μ₂)t):
Population of annuity recipients in the scheme influenced by the internal factors like the joining rate of new pensioners(λ₂) and the death rate of pensioners(μ₂).

∫ (term₃ + term₄) dt:
Population of annuity recipients. 

⸻

📌 Variables

Symbol	Description

ε₁, ε₂	Entry rates into contributors/pension influenced by external factors like government policies. 

λ₁, λ₂	Contributor and pensioner growth rates

μ₁, μ₂	Contributor and pensioner exit/death rates

t: time in months. 



⸻
