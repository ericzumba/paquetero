(ns paquetero-cli.core
  (:require [clojure.tools.cli :refer [parse-opts]])
  (:gen-class))

(def cli-options {})

(defn -main
  [& args]
  (let [{:keys [options arguments errors summary]} (parse-opts args cli-options)]))
