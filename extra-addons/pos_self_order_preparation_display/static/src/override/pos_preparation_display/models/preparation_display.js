import { patch } from "@web/core/utils/patch";
import { PreparationDisplay } from "@pos_preparation_display/app/models/preparation_display";

patch(PreparationDisplay.prototype, {
    async setup(data, env, preparationDisplayId) {
        await super.setup(...arguments);
        this.configPaperStatus = data.config_paper_status;
    },
});
