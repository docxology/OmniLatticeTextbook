# Question Bank — PDVSA Gateway Ops: The EGS Lattice-Linear Companion {#sec:q_part_III_pdvsa-gateway}

Linked chapter: [@sec:part_III_pdvsa-gateway].

## Recall

1. What is the PDVSA Gateway Ops artifact, exactly as the honesty-first
   disclaimer files it? *(Answer: a *simulator* and catalog map — not live
   PDVSA telemetry and not a Protokol Sistemas contract audit; each takeaway
   card opens the backing paper (math + empirics), not a measured oilfield
   SLA, and the IBM SNA ↔ TCP/IP gateway case study is the *historical
   rhyme*, not the product name [@mendez2026pdvsaMockup].)*
2. Name the four enterprise domain cards of the gateway console, the system
   each maps to, and the object that joins them. *(Answer: Production (ERP),
   Field (SCADA), Compliance (Legal), Export (Logistics), joined on one
   incident object; clicking a domain pulls it into the shared brief while
   the other domains stay lit — no tab reset [@mendez2026pdvsaGateway].)*
3. What is the ops decision cycle, what are its three sub-labels, and what is
   its relationship to MCA? *(Answer: Gather → Decide → Act — "signals in" →
   "one next action" → "execute & notify"; it is the console rendering of the
   MCA cycle Metabolize → Crystallize → Animate, filed as the mechanism that
   "turns incident noise into a next-action band" — forecasting as
   operational rehearsal, not prophecy [@mendez2026pdvsaGateway;
   @mendez2026pdvsaMockup].)*

## Application

4. Using the flow ramp of [@eq:part_III_pdvsa-gateway_model], $F_i = i \cdot
   r$, compute the profile for $n = 5$ steps at rate $r = 2$ by hand, and
   state what `textbook.models.lattice_linear_profile(5, 2)` returns.
   *(Answer: $F_1 = 2, F_2 = 4, F_3 = 6, F_4 = 8, F_5 = 10$, i.e. the ramp
   $2, 4, 6, 8, 10$; the function returns exactly $[2, 4, 6, 8, 10]$ — the
   $n$-th value sits at $n \cdot r$
   [@mendez2026pdvsaGateway].)*
5. Place each console caption in its correct data-locality zone: "ERP / SCADA
   enclosure", "Lattice joins domains here", "safe summary out · no core
   dump". *(Answer: Plant systems ↔ Integration bridge ↔ Partners & export,
   respectively — the three-zone topology in which the enclosure stays
   protected while the gateway mediates continuity toward partners
   [@mendez2026pdvsaGateway].)*
6. Two of the gateway's numeric takeaways are the savings claim (context cost
   under 15% of flat token dumps at $N \geq 6$) and the harmony claim (high
   coherence at $K = 12$). What evidentiary status does the page assign them,
   *(Answer: labelled simulator gains backed by companion empirics — not
   measured oilfield SLAs; the labelling forbids reading either number as a
   production deployment measurement of PDVSA operations
   [@mendez2026pdvsaGateway].)*

## Synthesis

7. The mockup's lede calls the SNA ↔ TCP/IP case study a "historical rhyme"
   and $\Phi \approx 1.618$ "Lattice-Linear routing grammar". Assemble these
   into a one-paragraph account of how the corpus uses analogies and
   constants without converting them into claims. *(Answer: both are filed as
   framing, not fact — the rhyme situates the gateway in engineering history
   (SNA Core vs Edge handoffs) while the meta description insists the page is
   "not live PDVSA telemetry", and $\Phi$ is filed as routing *grammar* for
   the console rather than as a measured constant of oilfield flows. In both
   cases the corpus labels the status of the construct at the point of use —
   rhyme, grammar, simulator — so the reader can separate catalog structure
   from operational claim, the same discipline the chapter's honesty-first
   section enforces [@mendez2026pdvsaMockup; @mendez2026pdvsaGateway].)*
8. The gateway's flow ramp is exactly linear ($F_n = n \cdot r$), yet the
   corpus also files $\Phi$-compounding octaves elsewhere (e.g.
   [@sec:part_0_octave-map]). Explain what work each construct does and why
   the gateway needs the linear one. *(Answer: the octave ladder $\Omega_n =
   \Phi^n \Omega_0$ ranks registers on a compounding exponential scale, while
   the gateway ramp is a deterministic per-step routing profile — step $i$
   carries $i \cdot r$, so the executive thread advances by fixed increments
   and doubling the rate doubles every value; with $\Phi \approx 1.618$ as
   the rate the profile is $i\Phi$, not $\Phi^i$ ($\Phi^3 \approx 4.236068$
   would be a ladder value). The gateway needs linearity because its claim is
   coordination of $N$ domains in one thread — a schedule — not growth
   [@mendez2026pdvsaGateway; @mendez2026pdvsaMockup].)*
9. The mockup files the gateway on the engine shelf as the "enterprise
   gateway companion", noting engine inclusion of the AGENT_SYNC sync-stack
   and a Lattice Chat workstream while it "does not displace the CMOS pin".
   Sketch how the gateway consumes upstream part III constructs and feeds
   downstream ones, naming one construct in each direction. *(Answer:
   upstream, it borrows the substrate-layer discipline of the CMOS protonic
   filing — its companion status is defined relative to that pin
   ([@sec:part_III_cmos-protonic] [@mendez2026cmosProtonic]) — and it routes
   multi-domain work the way the moving-up-stack chapter argues the lattice
   serves as the next AI layer ([@sec:part_III_moving-up-stack]); downstream,
   part III consumers include the reality-bridge's router vocabulary
   ([@sec:part_III_reality-bridge]), with the single-shared-brief incident
   object prefiguring stack-level integration
   [@mendez2026pdvsaMockup].)*
