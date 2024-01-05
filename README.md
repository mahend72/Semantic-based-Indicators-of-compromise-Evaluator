# Semantic-based-Indicators-of-compromise-Evaluator

T# IOC Evaluator for Additive Manufacturing (AM) Supply Chain

## Overview

This tool presents a novel Indicators of Compromise (IOC) Evaluator designed to monitor and detect disruptions and anomalies within the Additive Manufacturing (AM) supply chain. Leveraging Cyber Threat Intelligence (CTI) and cyber threat susceptibility analysis, the system assesses potential risks and prioritizes threats unique to the AM ecosystem.

## Research Problem

The AM supply chain faces distinctive vulnerabilities due to intricate interactions between physical and digital infrastructure. Existing threat detection solutions often struggle to identify these vulnerabilities and effectively analyze emerging threats within this context. This research addresses this problem by developing a dedicated system for AM that:

- Gathers and assesses IOCs and qualitative threat information.
- Analyzes complex relationships between IOCs using Heterogeneous Information Networks (HINs).
- Prioritizes threats based on their potential impact and exploitability within the AM supply chain.

## Motivation

The motivation for this research arises from the critical need to strengthen AM cybersecurity and ensure the resilience of its supply chain. Potential disruptions and anomalies caused by cyberattacks can have significant consequences, including:

- Intellectual property theft.
- Manufacturing of counterfeit or defective parts.
- Data breaches and exfiltration.
- Sabotage and operational disruptions.

The proposed IOC Evaluator aims to mitigate these risks by providing a targeted and effective approach to threat detection and analysis within the AM context.

## Threat Impact Visualiser (TIV)

### Functionality

The Threat Impact Visualiser (TIV) is the first component of the IOC Evaluator, responsible for:

- Collecting CTI feeds from AlienVault OTX.
- Analyzing IOCs using Heterogeneous Information Networks (HINs) and Graph Convolution Networks (GCNs).
- Identifying hidden associations and patterns between IOCs.
- Visualizing the threat landscape and interconnectedness of IOCs.

By understanding the complex relationships between threats, the TIV enables informed decision-making and proactive cybersecurity measures within the AM supply chain.

## Risk Exposure Analyser (REA)

### Functionality

The Risk Exposure Analyser (REA) acts as the second component of the IOC Evaluator, focusing on:

- Evaluating the likelihood of IOCs using eigenvector centrality.
- Considering potential consequences of each IOC based on severity and impact.
- Prioritizing IOCs based on their combined likelihood and impact.

This analysis allows AM operators to focus their resources on the most critical threats and implement efficient risk mitigation strategies.

## IOC Evaluator

The overall IOC Evaluator combines the functionalities of the TIV and REA to provide a comprehensive threat detection and analysis system for the AM supply chain. This system facilitates:

- Proactive threat detection and identification.
- Accurate threat impact estimation.
- Prioritization of high-risk threats for effective response.
- Enhanced resilience against potential disruptions and anomalies.

By integrating CTI and cyber threat susceptibility approaches, the IOC Evaluator offers a valuable tool for improving AM cybersecurity and safeguarding its critical infrastructure.
