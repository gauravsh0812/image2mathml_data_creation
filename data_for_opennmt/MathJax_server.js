const express = require('express');
const mjAPI = require("mathjax-node");
const _ = require('lodash');

// ==== Initialize the express server ==========================================
var app = express();
app.use(express.json());
// =============================================================================

// ==== Configure and start the MathJax API ====================================
function configureMathJax() {
    try {
        mjAPI.config({
            tex:
                {
                    MaxBuffer: 100000,
                    extensions: ["amsfonts.js", "amsbsy.js", "amsmath.js", "amssymb.js", "mathtools.js"]
                },

            MathJax:
                {
                    loader: {load: ['input/tex']}
                }
        });

        mjAPI.start();
    }
    catch (error) {
        console.error(`An error occurred while configuring MathJax: ${error.message}`);
        configureMathJax();
    }
}

configureMathJax();

// =============================================================================

/**
 * Create a MathJax laTeX convserion promise for the current TeX input. Return
 * this promise to be executed by the callee.
 * @param  {String} tex      The LaTeX equation string to be processed
 * @return {Promise}         A promise that includes the .mml attr after resolution
 *
 */

function tex2mml(tex) {
    try {
        my_promise = mjAPI.typeset({math: tex, format: "TeX", mml: true});

    } catch (error) {
        my_promise = new Promise(() => {
            throw `Error occurred during MJx typesetting:\n{error}`;
        });
    }
    return my_promise;
}

// Process a single TeX equation string into a MathML string
app.post('/tex2mml', function (req, res) {
    // Access the LaTeX source from the request object
    var tex_str = JSON.parse(req.body.tex_src)
    tex2mml(tex_str)
        .then((data) => {
            res.send(JSON.stringify(data.mml));
        })
        .catch((err) => {
            res.send(JSON.stringify(`FAILED::${err}::${tex_str}`));
        });
});

// Process a batch of TeX equation strings into corresponding MathML strings
app.post('/bulk_tex2mml', function (req, res) {
    var mjax_promises = _.map(JSON.parse(req.body.TeX_data), tex2mml);
    Promise.all(mjax_promises).then(function (result) {
        res.send(JSON.stringify(_.map(result, (data) => {
            return data.mml;
        })));
    });
});

// Restart the MathJax service
app.get('/restart', function (req, res) {
    console.log("MathJax service restarting");
    mjAPI.config({stopAfterTypeset: true});
    configureMathJax();
    res.send("MathJax service restarted");
});


// Start the express application server
var server = app.listen(8081, function () {
    var port = server.address().port
    console.log("MathJax server listening at http://localhost:%s", port)
});
