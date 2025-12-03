document.addEventListener("DOMContentLoaded", function () {

    /* Tipo de usuário */
    const tipoSelect = document.getElementById("tipo");
    const campoSenha = document.getElementById("campoSenhaAcesso");

    function mostrarCampoSenha() {
        const tipo = tipoSelect.value;
        if (tipo == "professor"){
            campoSenha.style.display = tipo === "professor" ? "flex" : "none";
        }
        if (tipo == "organizador") {
            campoSenha.style.display = tipo === "organizador" ? "flex" : "none";
        }
        if (tipo == "estudante") {
            campoSenha.style.display = "none";
        }
    }

    if (tipoSelect) {
        tipoSelect.addEventListener("change", mostrarCampoSenha);
    }
    

    /* --------------------------------------------------------------------------- */
    /* --------------------------------------------------------------------------- */


    /* MODAIS PARA DETALHES */
    const botoesDetalhes = document.querySelectorAll(".botao-detalhe, .botao-detalhe-tabela-evento");
    const modais = document.querySelectorAll(".evento-modal, .modal-evento");

    botoesDetalhes.forEach(botao => {
        botao.addEventListener("click", () => {
            const eventoId = botao.getAttribute("data-evento-id");
            const modal = document.getElementById(`modal-${eventoId}`);
            if (modal) modal.style.display = "flex";
        });
    });

    modais.forEach(modal => {
        const fechar = modal.querySelector(".fechar-modal, .fechar-modal-evento");
        if (fechar) {
            fechar.addEventListener("click", () => {
                modal.style.display = "none";
            });
        }

        modal.addEventListener("click", e => {
            if (e.target === modal) {
                modal.style.display = "none";
            }
        });
    });


    /* --------------------------------------------------------------------------- */
    /* --------------------------------------------------------------------------- */


    /* PADRÃO DAS MENSAGENS DO TOASTIFY */
    function message(text, background) {
        Toastify({
            text: text,
            duration: 3000,
            style: {
                background: background,
                boxShadow: "none"
            }
        }).showToast();
    }

    document.addEventListener("click", function(e) {
        const btn = e.target.closest(".eventos-inscricao-btn");
        if (!btn) return;

        e.preventDefault();

        const vagas = parseInt(btn.getAttribute("data-vagas"));
        const form = btn.closest("form");

        if (vagas <= 0) { /*MENSAGEM DE ERRO VAGAS ESGOTADAS*/
            message("Não há mais vagas disponíveis para este evento!", "linear-gradient(to top, #d83745ff, #b61919ff)");
            return; 
        }

            /* MENSAGEM DE INSCRIÇÃO */
            message("Inscrição do evento realizada com sucesso!", "linear-gradient(to top, #2ec03aff, #157933ff)");
            setTimeout(() => {
                form.submit();
            }, 2000);
    });
});




