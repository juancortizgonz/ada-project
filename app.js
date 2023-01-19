/* 
 * Author: Juan Camilo Ortiz G.
 * Repo: https://github.com/juancortizgonz/ada-project
*/
(function () {
    'use strict';

    /* 
     * Constructor of the data structure
    */
    function buildDisjointSet() {
        return new DisjointSet();
    }

    /* 
     * Initializes values to create a new instance
     */
    function DisjointSet() {
        this.clearFields();
    }

    DisjointSet.prototype = {
        /* 
         * Generate a set with the element that is passed as an argument or add it to the actual set
         * elem:<int> | The value that will be stored in the set
         * @returns boolean /-> True: if the element is successfully added
         *                  /-> False: if the element wasn't added to the set
         */
        makeSet: function (elem) {
            return true;
        },

        /* 
         * Get the representative element of the set
         */

    };
}
)();