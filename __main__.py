import sys
sys.path.append("C:\\Users\\adria\\OneDrive\\Documentos\\24-25\\1er_SEMESTRE\\IA\\GIT\\ia_2024")

from practica import agent, joc


def main():
    mida = (12, 12)

    agents = [
        agent.Viatger("Agent 1", mida_taulell=mida),
        agent.Viatger("Agent 2", mida_taulell=mida),
    ]

    lab = joc.Laberint(agents, mida_taulell=mida)

    lab.comencar()


if __name__ == "__main__":
    main()
