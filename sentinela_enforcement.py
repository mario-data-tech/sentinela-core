import json

class PolicyEnforcementEngine:
    """Motor de cumplimiento de políticas para el ecosistema Mario Data Tech."""
    
    def __init__(self):
        # Cargamos las reglas basadas en tu agent-gateway-policy.md
        self.risk_matrix = {
            "LOW": {"allow_auto": True, "requires_approval": False},
            "MEDIUM": {"allow_auto": True, "requires_approval": False},
            "HIGH": {"allow_auto": False, "requires_approval": True},
            "CRITICAL": {"allow_auto": False, "requires_approval": True}
        }

    def evaluate_action(self, agent_id: str, action: str, risk_level: str, tenant_id: str) -> dict:
        risk = risk_level.upper()
        if risk not in self.risk_matrix:
            risk = "CRITICAL"  # Por defecto ante riesgos desconocidos
            
        policy = self.risk_matrix[risk]
        
        if policy["allow_auto"]:
            decision = "ALLOW"
            reason = f"Acción de bajo/medio riesgo permitida automáticamente para el agente {agent_id}."
        else:
            decision = "DENY"
            reason = f"BLOQUEO DE SEGURIDAD: La acción '{action}' con nivel {risk} requiere aprobación explícita de un operador (Tenant: {tenant_id})."
            
        audit_event = {
            "event": "policy_evaluation",
            "tenant_id": tenant_id,
            "agent_id": agent_id,
            "action": action,
            "risk_level": risk,
            "policy_decision": decision,
            "reason": reason
        }
        
        return audit_event

if __name__ == "__main__":
    print("--- PROBANDO MOTOR DE ENFORCEMENT DE SENTINELA ---")
    engine = PolicyEnforcementEngine()
    
    # Prueba 1: Acción de riesgo bajo (Debe permitir)
    res_low = engine.evaluate_action("nexus-01", "read_logs", "LOW", "tenant-mario-01")
    print(json.dumps(res_low, indent=2))
    
    # Prueba 2: Acción de riesgo alto (Debe denegar y exigir aprobación)
    res_high = engine.evaluate_action("auditflow-agent", "modify_production_database", "HIGH", "tenant-mario-01")
    print(json.dumps(res_high, indent=2))
