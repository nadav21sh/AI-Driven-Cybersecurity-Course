# Lab 1 — Cyber Threat Intelligence (CTI) Report Mapping to MITRE ATT&CK

## Group Members
- Nadav Shapira (ID: 325363505)
- jordan levy (ID: 207905696)
## Source CTI Report
**Title:** Analyzing Solorigate: The Compromised DLL File That Started a Sophisticated Cyberattack  
**Source:** Microsoft Security Blog  
**Link:** https://www.microsoft.com/security/blog/2020/12/13/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack/

## Short Attack Summary
The SolarWinds SUNBURST (also known as Solorigate) attack was a highly sophisticated supply chain compromise attributed to a nation-state threat actor. The attackers gained access to SolarWinds’ software build environment and inserted a malicious backdoor into legitimate Orion platform updates. These trojanized updates were digitally signed and distributed to thousands of customers, including government agencies and large enterprises. Once installed, the malware executed as a trusted service and remained dormant for up to two weeks to evade detection. SUNBURST used stealthy, DNS-based command-and-control communications and selectively activated only on high-value targets. After activation, the attackers performed reconnaissance, lateral movement, credential abuse, and data exfiltration. This attack is significant because it demonstrated how trusted software supply chains can be abused to bypass traditional security controls and remain undetected for long periods.

## Attack Diagram / Sequence
```
[Attacker]
    |
    v
[Compromise SolarWinds Build Environment]
    |
    v
[Insert SUNBURST Backdoor into Orion DLL]
    |
    v
[Digitally Sign Malicious Update]
    |
    v
[Distribute Trojanized Orion Updates]
    |
    v
[Victim Organization Installs Update]
    |
    v
[SUNBURST Executes as Trusted Service]
    |
    v
[Dormant Period / Defense Evasion]
    |
    v
[DNS-based Command & Control]
    |
    v
[Target Profiling & Victim Selection]
    |
    v
[Lateral Movement & Credential Abuse]
    |
    v
[Data Collection and Exfiltration]
```

## MITRE ATT&CK Mapping

| Tactic | Technique | Behavior from the Report | ATT&CK Link |
|-------|-----------|--------------------------|-------------|
| Reconnaissance | Gather Victim Org Information (T1591) | SUNBURST collected domain, IP, and environment details to identify high-value targets | https://attack.mitre.org/techniques/T1591/ |
| Resource Development | Supply Chain Compromise (T1195) | Malicious code was inserted into SolarWinds Orion software updates | https://attack.mitre.org/techniques/T1195/ |
| Initial Access | Trusted Relationship (T1199) | Victims trusted SolarWinds updates, enabling initial access | https://attack.mitre.org/techniques/T1199/ |
| Execution | Command and Scripting Interpreter (T1059) | Malicious code executed within the SolarWinds service context | https://attack.mitre.org/techniques/T1059/ |
| Persistence | Boot or Logon Autostart Execution (T1547) | SUNBURST ensured execution by loading when Orion services started | https://attack.mitre.org/techniques/T1547/ |
| Privilege Escalation | Abuse Elevation Control Mechanism (T1548) | Attackers leveraged existing service privileges to operate at high integrity | https://attack.mitre.org/techniques/T1548/ |
| Defense Evasion | Signed Binary Proxy Execution (T1218) | Use of digitally signed SolarWinds binaries to evade security controls | https://attack.mitre.org/techniques/T1218/ |
| Defense Evasion | Obfuscated/Encrypted Payloads (T1027) | Malware used obfuscation and delayed execution to avoid detection | https://attack.mitre.org/techniques/T1027/ |
| Credential Access | Credential Dumping (T1003) | Follow-on activity included credential harvesting in compromised networks | https://attack.mitre.org/techniques/T1003/ |
| Discovery | Network Service Discovery (T1046) | Attackers mapped internal networks after initial compromise | https://attack.mitre.org/techniques/T1046/ |
| Lateral Movement | Remote Services (T1021) | Use of stolen credentials to access additional systems | https://attack.mitre.org/techniques/T1021/ |
| Command and Control | Application Layer Protocol: DNS (T1071.004) | SUNBURST communicated with C2 servers using DNS queries | https://attack.mitre.org/techniques/T1071/004/ |
| Exfiltration | Exfiltration Over C2 Channel (T1041) | Data was exfiltrated using the established C2 infrastructure | https://attack.mitre.org/techniques/T1041/ |
| Impact | Data Manipulation (T1565) | Potential modification and abuse of sensitive systems and data | https://attack.mitre.org/techniques/T1565/ |

## Insights / What I Learned
This attack shows how mapping CTI reports to MITRE ATT&CK provides a structured way to understand adversary behavior across the entire kill chain. The SolarWinds incident highlights the extreme risk posed by supply chain compromises and trusted relationships. Using ATT&CK mapping helps defenders identify detection gaps and prioritize controls beyond perimeter-based security.

