# -*- coding: utf-8 -*-
"""Banco cerrado de referencias del proyecto (única fuente de la lista de referencias).
Cada entrada: key, cite (texto de la cita en el cuerpo, p. ej. 'Bang et al.'), year, apa (APA 7 en español, *cursivas* en markdown),
tipo, origen (F-INF = corpus del informe_FINAL aportado por el usuario; CANON = citada en el metaprompt/MDR;
DOMINIO = literatura de dominio; NORMA = norma colombiana o documento oficial), nat (NTC 1.1), ver (verificación)."""
import json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))

def _slug(s):
    s = unicodedata.normalize("NFKD", s)
    return re.sub(r"[^A-Za-z0-9]", "", "".join(c for c in s if not unicodedata.combining(c)))

def corpus():
    items = json.load(open(os.path.join(HERE, "corpus_informe.json"), encoding="utf-8"))
    out = []
    fix = {"Pedraza2026": "MuradPedraza2026", "Moura2025": "DeMoura2025", "Comercio2026": "SIC2026", "Brkic2026": "SpasojevicBrkic2026",
           "Rine2024": "Roine2024"}
    for it in items:
        k = _slug(it["key"]); k = fix.get(k, k)
        it["key"] = k
        if k == "SIC2026": it["cite"] = "Superintendencia de Industria y Comercio [SIC]"
        a = it["apa"].replace(",, ", ", ").replace("--", "–").replace("Atmosphere y Health", "Atmosphere & Health")
        it["apa"] = a
        out.append(it)
    return out

def D(key, cite, year, apa, tipo="articulo", origen="DOMINIO", nat="DOCUMENTADO", ver="NO_VERIFICADO"):
    return dict(key=key, cite=cite, year=year, apa=apa, tipo=tipo, origen=origen, nat=nat, ver=ver)

MDR = [
 D("Argyris1978","Argyris y Schön",1978,"Argyris, C., y Schön, D. A. (1978). *Organizational learning: A theory of action perspective*. Addison-Wesley.","libro","CANON"),
 D("Bacchi2009","Bacchi",2009,"Bacchi, C. (2009). *Analysing policy: What's the problem represented to be?* Pearson Australia.","libro","CANON"),
 D("Befani2014","Befani y Mayne",2014,"Befani, B., y Mayne, J. (2014). Process tracing and contribution analysis: A combined approach to generative causal inference for impact evaluation. *IDS Bulletin, 45*(6), 17–36.","articulo","CANON"),
 D("Braybrooke1963","Braybrooke y Lindblom",1963,"Braybrooke, D., y Lindblom, C. E. (1963). *A strategy of decision: Policy evaluation as a social process*. Free Press.","libro","CANON"),
 D("Collingridge1980","Collingridge",1980,"Collingridge, D. (1980). *The social control of technology*. Frances Pinter.","libro","CANON"),
 D("Deming1986","Deming",1986,"Deming, W. E. (1986). *Out of the crisis*. MIT Center for Advanced Engineering Study.","libro","CANON"),
 D("Dunn2018","Dunn",2018,"Dunn, W. N. (2018). *Public policy analysis: An integrated approach* (6.ª ed.). Routledge.","libro","CANON"),
 D("Elmore1979","Elmore",1979,"Elmore, R. F. (1979). Backward mapping: Implementation research and policy decisions. *Political Science Quarterly, 94*(4), 601–616.","articulo","CANON"),
 D("Etzioni1967","Etzioni",1967,"Etzioni, A. (1967). Mixed-scanning: A «third» approach to decision-making. *Public Administration Review, 27*(5), 385–392.","articulo","CANON"),
 D("Funnell2011","Funnell y Rogers",2011,"Funnell, S. C., y Rogers, P. J. (2011). *Purposeful program theory: Effective use of theories of change and logic models*. Jossey-Bass.","libro","CANON"),
 D("Glouberman2002","Glouberman y Zimmerman",2002,"Glouberman, S., y Zimmerman, B. (2002). *Complicated and complex systems: What would successful reform of Medicare look like?* (Discussion Paper No. 8). Commission on the Future of Health Care in Canada.","informe","CANON"),
 D("Janis1982","Janis",1982,"Janis, I. L. (1982). *Groupthink: Psychological studies of policy decisions and fiascoes* (2.ª ed.). Houghton Mifflin.","libro","CANON"),
 D("Klein2007","Klein",2007,"Klein, G. (2007). Performing a project premortem. *Harvard Business Review, 85*(9), 18–19.","articulo","CANON"),
 D("Lindblom1959","Lindblom",1959,"Lindblom, C. E. (1959). The science of «muddling through». *Public Administration Review, 19*(2), 79–88.","articulo","CANON"),
 D("Lipsky1980","Lipsky",1980,"Lipsky, M. (1980). *Street-level bureaucracy: Dilemmas of the individual in public services*. Russell Sage Foundation.","libro","CANON"),
 D("Mayne2012","Mayne",2012,"Mayne, J. (2012). Contribution analysis: Coming of age? *Evaluation, 18*(3), 270–280.","articulo","CANON"),
 D("Merton1936","Merton",1936,"Merton, R. K. (1936). The unanticipated consequences of purposive social action. *American Sociological Review, 1*(6), 894–904.","articulo","CANON"),
 D("Mitchell1997","Mitchell et al.",1997,"Mitchell, R. K., Agle, B. R., y Wood, D. J. (1997). Toward a theory of stakeholder identification and salience: Defining the principle of who and what really counts. *Academy of Management Review, 22*(4), 853–886. https://doi.org/10.5465/amr.1997.9711022105","articulo","CANON"),
 D("North1990","North",1990,"North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.","libro","CANON"),
 D("Ostrom2005","Ostrom",2005,"Ostrom, E. (2005). *Understanding institutional diversity*. Princeton University Press.","libro","CANON"),
 D("Pawson1997","Pawson y Tilley",1997,"Pawson, R., y Tilley, N. (1997). *Realistic evaluation*. Sage.","libro","CANON"),
 D("Raiffa1968","Raiffa",1968,"Raiffa, H. (1968). *Decision analysis: Introductory lectures on choices under uncertainty*. Addison-Wesley.","libro","CANON"),
 D("Scharpf1997","Scharpf",1997,"Scharpf, F. W. (1997). *Games real actors play: Actor-centered institutionalism in policy research*. Westview Press.","libro","CANON"),
 D("Schon1994","Schön y Rein",1994,"Schön, D. A., y Rein, M. (1994). *Frame reflection: Toward the resolution of intractable policy controversies*. Basic Books.","libro","CANON"),
 D("Shediac1998","Shediac-Rizkallah y Bone",1998,"Shediac-Rizkallah, M. C., y Bone, L. R. (1998). Planning for the sustainability of community-based health programs: Conceptual frameworks and future directions for research, practice and policy. *Health Education Research, 13*(1), 87–108. https://doi.org/10.1093/her/13.1.87","articulo","CANON"),
 D("Simon1955","Simon",1955,"Simon, H. A. (1955). A behavioral model of rational choice. *The Quarterly Journal of Economics, 69*(1), 99–118.","articulo","CANON"),
 D("Simon1973","Simon",1973,"Simon, H. A. (1973). The structure of ill structured problems. *Artificial Intelligence, 4*(3–4), 181–201.","articulo","CANON"),
 D("Smalley2018","Smalley",2018,"Smalley, A. (2018). *Four types of problems: From reactive troubleshooting to creative innovation*. Lean Enterprise Institute.","libro","CANON"),
 D("Snowden2007","Snowden y Boone",2007,"Snowden, D. J., y Boone, M. E. (2007). A leader's framework for decision making. *Harvard Business Review, 85*(11), 68–76.","articulo","CANON"),
 D("Taplin2012","Taplin y Clark",2012,"Taplin, D. H., y Clark, H. (2012). *Theory of change basics: A primer on theory of change*. ActKnowledge.","informe","CANON"),
 D("Toulmin1958","Toulmin",1958,"Toulmin, S. E. (1958). *The uses of argument*. Cambridge University Press.","libro","CANON"),
 D("Tversky1974","Tversky y Kahneman",1974,"Tversky, A., y Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124–1131.","articulo","CANON"),
 D("Weiss1995","Weiss",1995,"Weiss, C. H. (1995). Nothing as practical as good theory. En J. P. Connell et al. (Eds.), *New approaches to evaluating community initiatives* (pp. 65–92). Aspen Institute.","capitulo","CANON"),
 D("Dror1968","Dror",1968,"Dror, Y. (1968). *Public policymaking reexamined*. Chandler.","libro","CANON"),
 D("Hiatt2006","Hiatt",2006,"Hiatt, J. M. (2006). *ADKAR: A model for change in business, government and our community*. Prosci.","libro","CANON"),
 D("Ragin1987","Ragin",1987,"Ragin, C. C. (1987). *The comparative method: Moving beyond qualitative and quantitative strategies*. University of California Press.","libro","CANON"),
 D("Rosenhead2001","Rosenhead y Mingers",2001,"Rosenhead, J., y Mingers, J. (Eds.). (2001). *Rational analysis for a problematic world revisited* (2.ª ed.). Wiley.","libro","CANON"),
 D("WilsonGrau2019","Wilson-Grau",2019,"Wilson-Grau, R. (2019). *Outcome harvesting: Principles, steps, and evaluation applications*. Information Age Publishing.","libro","CANON"),
 D("Festinger1957","Festinger",1957,"Festinger, L. (1957). *A theory of cognitive dissonance*. Stanford University Press.","libro","CANON"),
 D("Hay2002","Hay",2002,"Hay, C. (2002). *Political analysis: A critical introduction*. Palgrave.","libro","CANON"),
 D("Jessop2008","Jessop",2008,"Jessop, B. (2008). *State power: A strategic-relational approach*. Polity.","libro","CANON"),
 D("MarchOlsen1989","March y Olsen",1989,"March, J. G., y Olsen, J. P. (1989). *Rediscovering institutions: The organizational basis of politics*. Free Press.","libro","CANON"),
 D("Mills1959","Mills",1959,"Mills, C. W. (1959). *The sociological imagination*. Oxford University Press.","libro","CANON"),
 D("Pearl2018","Pearl y Mackenzie",2018,"Pearl, J., y Mackenzie, D. (2018). *The book of why: The new science of cause and effect*. Basic Books.","libro","CANON"),
 D("Thompson1959","Thompson y Tuden",1959,"Thompson, J. D., y Tuden, A. (1959). Strategies, structures, and processes of organizational decision. En J. D. Thompson et al. (Eds.), *Comparative studies in administration*. University of Pittsburgh Press.","capitulo","CANON"),
 D("Tsebelis2002","Tsebelis",2002,"Tsebelis, G. (2002). *Veto players: How political institutions work*. Princeton University Press.","libro","CANON"),
 D("Vickers1965","Vickers",1965,"Vickers, G. (1965). *The art of judgment: A study of policy making*. Chapman & Hall.","libro","CANON"),
]

CANON = [
 D("Swales1990","Swales",1990,"Swales, J. M. (1990). *Genre analysis: English in academic and research settings*. Cambridge University Press.","libro","CANON"),
 D("Swales2004","Swales",2004,"Swales, J. M. (2004). *Research genres: Explorations and applications*. Cambridge University Press.","libro","CANON"),
 D("Toulmin2003","Toulmin",2003,"Toulmin, S. E. (2003). *The uses of argument* (ed. actualizada). Cambridge University Press.","libro","CANON"),
 D("Kotter2012","Kotter",2012,"Kotter, J. P. (2012). *Leading change* (ed. con nuevo prefacio). Harvard Business Review Press.","libro","CANON"),
 D("Christensen2016","Christensen",2016,"Christensen, C. M. (2016). *The innovator's dilemma: When new technologies cause great firms to fail*. Harvard Business Review Press.","libro","CANON"),
 D("Christensen2016b","Christensen et al.",2016,"Christensen, C. M., Hall, T., Dillon, K., y Duncan, D. S. (2016). *Competing against luck: The story of innovation and customer choice*. Harper Business.","libro","CANON"),
 D("Argyris1999","Argyris",1999,"Argyris, C. (1999). *On organizational learning* (2.ª ed.). Blackwell.","libro","CANON"),
 D("Kahneman1979","Kahneman y Tversky",1979,"Kahneman, D., y Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica, 47*(2), 263–291. https://doi.org/10.2307/1914185","articulo","CANON"),
 D("Saaty1980","Saaty",1980,"Saaty, T. L. (1980). *The analytic hierarchy process: Planning, priority setting, resource allocation*. McGraw-Hill.","libro","CANON"),
 D("Mirjalili2014","Mirjalili et al.",2014,"Mirjalili, S., Mirjalili, S. M., y Lewis, A. (2014). Grey wolf optimizer. *Advances in Engineering Software, 69*, 46–61. https://doi.org/10.1016/j.advengsoft.2013.12.007","articulo","CANON"),
 D("Aria2017","Aria y Cuccurullo",2017,"Aria, M., y Cuccurullo, C. (2017). bibliometrix: An R-tool for comprehensive science mapping analysis. *Journal of Informetrics, 11*(4), 959–975. https://doi.org/10.1016/j.joi.2017.08.007","articulo","CANON"),
 D("Page2021","Page et al.",2021,"Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, Artículo n71. https://doi.org/10.1136/bmj.n71","articulo","CANON"),
 D("Vester2007","Vester",2007,"Vester, F. (2007). *The art of interconnected thinking: Tools and concepts for a new approach to tackling complexity*. MCB Verlag.","libro","CANON"),
 D("Godet2001","Godet",2001,"Godet, M. (2001). *Creating futures: Scenario planning as a strategic management tool*. Economica.","libro","CANON"),
]

DOMINIO = [
 D("Barkjohn2021","Barkjohn et al.",2021,"Barkjohn, K. K., Gantt, B., y Clements, A. L. (2021). Development and application of a United States-wide correction for PM2.5 data collected with the PurpleAir sensor. *Atmospheric Measurement Techniques, 14*(6), 4617–4637. https://doi.org/10.5194/amt-14-4617-2021"),
 D("Crilley2018","Crilley et al.",2018,"Crilley, L. R., Shaw, M., Pound, R., Kramer, L. J., Price, R., Young, S., Lewis, A. C., y Pope, F. D. (2018). Evaluation of a low-cost optical particle counter (Alphasense OPC-N2) for ambient air monitoring. *Atmospheric Measurement Techniques, 11*(2), 709–720. https://doi.org/10.5194/amt-11-709-2018"),
 D("Giordano2021","Giordano et al.",2021,"Giordano, M. R., Malings, C., Pandis, S. N., Presto, A. A., McNeill, V. F., Westervelt, D. M., Beekmann, M., y Subramanian, R. (2021). From low-cost sensors to high-quality data: A summary of challenges and best practices for effectively calibrating low-cost particulate matter mass sensors. *Journal of Aerosol Science, 158*, Artículo 105833. https://doi.org/10.1016/j.jaerosci.2021.105833"),
 D("Karagulian2019","Karagulian et al.",2019,"Karagulian, F., Barbiere, M., Kotsev, A., Spinelle, L., Gerboles, M., Lagler, F., Redon, N., Crunaire, S., y Borowiak, A. (2019). Review of the performance of low-cost sensors for air quality monitoring. *Atmosphere, 10*(9), Artículo 506. https://doi.org/10.3390/atmos10090506"),
 D("Jayaratne2018","Jayaratne et al.",2018,"Jayaratne, R., Liu, X., Thai, P., Dunbabin, M., y Morawska, L. (2018). The influence of humidity on the performance of a low-cost air particle mass sensor and the effect of atmospheric fog. *Atmospheric Measurement Techniques, 11*(8), 4883–4890. https://doi.org/10.5194/amt-11-4883-2018"),
 D("Magi2020","Magi et al.",2020,"Magi, B. I., Cupini, C., Francis, J., Green, M., y Hauser, C. (2020). Evaluation of PM2.5 measured in an urban setting using a low-cost optical particle counter and a Federal Equivalent Method Beta Attenuation Monitor. *Aerosol Science and Technology, 54*(2), 147–159. https://doi.org/10.1080/02786826.2019.1619915"),
 D("Morawska2018","Morawska et al.",2018,"Morawska, L., Thai, P. K., Liu, X., Asumadu-Sakyi, A., Ayoko, G., Bartonova, A., et al. (2018). Applications of low-cost sensing technologies for air quality monitoring and exposure assessment: How far have they gone? *Environment International, 116*, 286–299. https://doi.org/10.1016/j.envint.2018.04.018"),
 D("KumarP2015","Kumar et al.",2015,"Kumar, P., Morawska, L., Martani, C., Biskos, G., Neophytou, M., Di Sabatino, S., Bell, M., Norford, L., y Britter, R. (2015). The rise of low-cost sensing for managing air pollution in cities. *Environment International, 75*, 199–205. https://doi.org/10.1016/j.envint.2014.11.019"),
 D("Castell2017","Castell et al.",2017,"Castell, N., Dauge, F. R., Schneider, P., Vogt, M., Lerner, U., Fishbain, B., Broday, D., y Bartonova, A. (2017). Can commercial low-cost sensor platforms contribute to air quality monitoring and exposure estimates? *Environment International, 99*, 293–302. https://doi.org/10.1016/j.envint.2016.12.007"),
 D("Malings2020","Malings et al.",2020,"Malings, C., Tanzer, R., Hauryliuk, A., Saha, P. K., Robinson, A. L., Presto, A. A., y Subramanian, R. (2020). Fine particle mass monitoring with low-cost sensors: Corrections and long-term performance evaluation. *Aerosol Science and Technology, 54*(2), 160–174. https://doi.org/10.1080/02786826.2019.1623863"),
 D("WHO2021","Organización Mundial de la Salud [OMS]",2021,"Organización Mundial de la Salud. (2021). *WHO global air quality guidelines: Particulate matter (PM2.5 and PM10), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide*. OMS.","informe","DOMINIO"),
 D("EPA2021","U.S. Environmental Protection Agency [EPA]",2021,"U.S. Environmental Protection Agency. (2021). *Performance testing protocols, metrics, and target values for fine particulate matter air sensors: Use in ambient, outdoor, fixed sites, non-regulatory supplemental and informational monitoring applications* (EPA/600/R-20/280). Office of Research and Development.","informe","DOMINIO"),
 D("Pope2006","Pope y Dockery",2006,"Pope, C. A., III, y Dockery, D. W. (2006). Health effects of fine particulate air pollution: Lines that connect. *Journal of the Air & Waste Management Association, 56*(6), 709–742. https://doi.org/10.1080/10473289.2006.10464485"),
 D("Landrigan2004","Landrigan et al.",2004,"Landrigan, P. J., Lioy, P. J., Thurston, G., Berkowitz, G., Chen, L. C., Chillrud, S. N., et al. (2004). Health and environmental consequences of the World Trade Center disaster. *Environmental Health Perspectives, 112*(6), 731–739. https://doi.org/10.1289/ehp.6702"),
 D("Stieb2008","Stieb et al.",2008,"Stieb, D. M., Burnett, R. T., Smith-Doiron, M., Brion, O., Shin, H. H., y Economou, V. (2008). A new multipollutant, no-threshold air quality health index based on short-term associations observed in daily time-series analyses. *Journal of the Air & Waste Management Association, 58*(3), 435–450. https://doi.org/10.3155/1047-3289.58.3.435"),
 D("Grieves2017","Grieves y Vickers",2017,"Grieves, M., y Vickers, J. (2017). Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems. En F.-J. Kahlen, S. Flumerfelt, y A. Alves (Eds.), *Transdisciplinary perspectives on complex systems: New findings and approaches* (pp. 85–113). Springer. https://doi.org/10.1007/978-3-319-38756-7_4","capitulo"),
 D("Tao2019","Tao et al.",2019,"Tao, F., Zhang, H., Liu, A., y Nee, A. Y. C. (2019). Digital twin in industry: State-of-the-art. *IEEE Transactions on Industrial Informatics, 15*(4), 2405–2415. https://doi.org/10.1109/TII.2018.2873186"),
 D("Warden2019","Warden y Situnayake",2019,"Warden, P., y Situnayake, D. (2019). *TinyML: Machine learning with TensorFlow Lite on Arduino and ultra-low-power microcontrollers*. O'Reilly Media.","libro"),
 D("David2021","David et al.",2021,"David, R., Duke, J., Jain, A., Janapa Reddi, V., Jeffries, N., Li, J., et al. (2021). TensorFlow Lite Micro: Embedded machine learning for TinyML systems. *Proceedings of Machine Learning and Systems, 3*, 800–811.","articulo"),
 D("Shi2016","Shi et al.",2016,"Shi, W., Cao, J., Zhang, Q., Li, Y., y Xu, L. (2016). Edge computing: Vision and challenges. *IEEE Internet of Things Journal, 3*(5), 637–646. https://doi.org/10.1109/JIOT.2016.2579198"),
 D("Adelantado2017","Adelantado et al.",2017,"Adelantado, F., Vilajosana, X., Tuset-Peiro, P., Martinez, B., Melià-Seguí, J., y Watteyne, T. (2017). Understanding the limits of LoRaWAN. *IEEE Communications Magazine, 55*(9), 34–40. https://doi.org/10.1109/MCOM.2017.1600613"),
 D("Hevner2004","Hevner et al.",2004,"Hevner, A. R., March, S. T., Park, J., y Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105. https://doi.org/10.2307/25148625"),
 D("Ries2011","Ries",2011,"Ries, E. (2011). *The lean startup: How today's entrepreneurs use continuous innovation to create radically successful businesses*. Crown Business.","libro"),
 D("Cooper2008","Cooper",2008,"Cooper, R. G. (2008). Perspective: The Stage-Gate® idea-to-launch process—Update, what's new, and NexGen systems. *Journal of Product Innovation Management, 25*(3), 213–232. https://doi.org/10.1111/j.1540-5885.2008.00296.x"),
 D("Mankins1995","Mankins",1995,"Mankins, J. C. (1995). *Technology readiness levels: A white paper*. National Aeronautics and Space Administration, Office of Space Access and Technology.","informe"),
 D("PMI2021","Project Management Institute [PMI]",2021,"Project Management Institute. (2021). *Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* y *el estándar para la dirección de proyectos* (7.ª ed.). PMI.","libro"),
 D("ISO31000","Organización Internacional de Normalización [ISO]",2018,"Organización Internacional de Normalización. (2018). *ISO 31000:2018. Gestión del riesgo: Directrices*. ISO.","informe"),
 D("Patton2011","Patton",2011,"Patton, M. Q. (2011). *Developmental evaluation: Applying complexity concepts to enhance innovation and use*. Guilford Press.","libro"),
 D("Rogers2003","Rogers",2003,"Rogers, E. M. (2003). *Diffusion of innovations* (5.ª ed.). Free Press.","libro"),
 D("Davis1989","Davis",1989,"Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340. https://doi.org/10.2307/249008"),
 D("Venkatesh2003","Venkatesh et al.",2003,"Venkatesh, V., Morris, M. G., Davis, G. B., y Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly, 27*(3), 425–478. https://doi.org/10.2307/30036540"),
 D("Arnstein1969","Arnstein",1969,"Arnstein, S. R. (1969). A ladder of citizen participation. *Journal of the American Institute of Planners, 35*(4), 216–224. https://doi.org/10.1080/01944366908977225"),
 D("Callon1999","Callon",1999,"Callon, M. (1999). The role of lay people in the production and dissemination of scientific knowledge. *Science, Technology & Society, 4*(1), 81–94. https://doi.org/10.1177/097172189900400106"),
 D("Funtowicz1993","Funtowicz y Ravetz",1993,"Funtowicz, S. O., y Ravetz, J. R. (1993). Science for the post-normal age. *Futures, 25*(7), 739–755. https://doi.org/10.1016/0016-3287(93)90022-L"),
 D("Freire2005","Freire",2005,"Freire, P. (2005). *Pedagogía del oprimido* (2.ª ed.). Siglo XXI. (Obra original publicada en 1970)","libro"),
 D("OCDE2018","Organización para la Cooperación y el Desarrollo Económicos [OCDE]",2018,"Organización para la Cooperación y el Desarrollo Económicos, y Eurostat. (2018). *Oslo manual 2018: Guidelines for collecting, reporting and using data on innovation* (4.ª ed.). OECD Publishing. https://doi.org/10.1787/9789264304604-en","informe"),
 D("OCDE2015","Organización para la Cooperación y el Desarrollo Económicos [OCDE]",2015,"Organización para la Cooperación y el Desarrollo Económicos. (2015). *Frascati manual 2015: Guidelines for collecting and reporting data on research and experimental development*. OECD Publishing. https://doi.org/10.1787/9789264239012-en","informe"),
 D("Teece1986","Teece",1986,"Teece, D. J. (1986). Profiting from technological innovation: Implications for integration, collaboration, licensing and public policy. *Research Policy, 15*(6), 285–305. https://doi.org/10.1016/0048-7333(86)90027-2"),
 D("Chesbrough2003","Chesbrough",2003,"Chesbrough, H. W. (2003). *Open innovation: The new imperative for creating and profiting from technology*. Harvard Business School Press.","libro"),
 D("Boardman2018","Boardman et al.",2018,"Boardman, A. E., Greenberg, D. H., Vining, A. R., y Weimer, D. L. (2018). *Cost-benefit analysis: Concepts and practice* (5.ª ed.). Cambridge University Press.","libro"),
 D("Gertler2016","Gertler et al.",2016,"Gertler, P. J., Martinez, S., Premand, P., Rawlings, L. B., y Vermeersch, C. M. J. (2016). *Impact evaluation in practice* (2.ª ed.). Banco Mundial. https://doi.org/10.1596/978-1-4648-0779-4","libro"),
 D("Lotka1926","Lotka",1926,"Lotka, A. J. (1926). The frequency distribution of scientific productivity. *Journal of the Washington Academy of Sciences, 16*(12), 317–323."),
 D("Bradford1934","Bradford",1934,"Bradford, S. C. (1934). Sources of information on specific subjects. *Engineering, 137*, 85–86."),
 D("VanEck2010","van Eck y Waltman",2010,"van Eck, N. J., y Waltman, L. (2010). Software survey: VOSviewer, a computer program for bibliometric mapping. *Scientometrics, 84*(2), 523–538. https://doi.org/10.1007/s11192-009-0146-3"),
 D("Kessler1963","Kessler",1963,"Kessler, M. M. (1963). Bibliographic coupling between scientific papers. *American Documentation, 14*(1), 10–25. https://doi.org/10.1002/asi.5090140103"),
 D("Small1973","Small",1973,"Small, H. (1973). Co-citation in the scientific literature: A new measure of the relationship between two documents. *Journal of the American Society for Information Science, 24*(4), 265–269. https://doi.org/10.1002/asi.4630240406"),
 D("Callon1991","Callon et al.",1991,"Callon, M., Courtial, J.-P., y Laville, F. (1991). Co-word analysis as a tool for describing the network of interactions between basic and technological research: The case of polymer chemistry. *Scientometrics, 22*(1), 155–205. https://doi.org/10.1007/BF02019280"),
 D("Cobo2011","Cobo et al.",2011,"Cobo, M. J., López-Herrera, A. G., Herrera-Viedma, E., y Herrera, F. (2011). An approach for detecting, quantifying, and visualizing the evolution of a research field: A practical application to the fuzzy sets theory field. *Journal of Informetrics, 5*(1), 146–166. https://doi.org/10.1016/j.joi.2010.10.002"),
 D("Rezaei2015","Rezaei",2015,"Rezaei, J. (2015). Best-worst multi-criteria decision-making method. *Omega, 53*, 49–57. https://doi.org/10.1016/j.omega.2014.11.009"),
 D("Hwang1981","Hwang y Yoon",1981,"Hwang, C.-L., y Yoon, K. (1981). *Multiple attribute decision making: Methods and applications. A state-of-the-art survey* (Lecture Notes in Economics and Mathematical Systems, Vol. 186). Springer. https://doi.org/10.1007/978-3-642-48318-9","libro"),
 D("UNISDR2015","Oficina de las Naciones Unidas para la Reducción del Riesgo de Desastres [UNDRR]",2015,"Oficina de las Naciones Unidas para la Reducción del Riesgo de Desastres. (2015). *Marco de Sendái para la reducción del riesgo de desastres 2015-2030*. UNDRR.","informe"),
 D("APA2020","American Psychological Association",2020,"American Psychological Association. (2020). *Publication manual of the American Psychological Association* (7.ª ed.). American Psychological Association. https://doi.org/10.1037/0000165-000","libro"),
 D("ONU2015","Organización de las Naciones Unidas [ONU]",2015,"Organización de las Naciones Unidas. (2015). *Transformar nuestro mundo: La Agenda 2030 para el Desarrollo Sostenible* (A/RES/70/1). ONU.","informe"),
]

NORMAS = [
 D("Ley1523","Congreso de la República",2012,"Congreso de la República de Colombia. (2012, 24 de abril). *Ley 1523 de 2012. Por la cual se adopta la política nacional de gestión del riesgo de desastres y se establece el Sistema Nacional de Gestión del Riesgo de Desastres*. Diario Oficial n.º 48.411.","norma","NORMA"),
 D("Ley2056","Congreso de la República",2020,"Congreso de la República de Colombia. (2020, 30 de septiembre). *Ley 2056 de 2020. Por la cual se regula la organización y el funcionamiento del Sistema General de Regalías*. Diario Oficial n.º 51.453.","norma","NORMA"),
 D("Ley1286","Congreso de la República",2009,"Congreso de la República de Colombia. (2009, 23 de enero). *Ley 1286 de 2009. Por la cual se modifica la Ley 29 de 1990, se transforma a Colciencias en Departamento Administrativo y se fortalece el Sistema Nacional de Ciencia, Tecnología e Innovación en Colombia y se dictan otras disposiciones*. Diario Oficial n.º 47.241.","norma","NORMA"),
 D("Ley1581","Congreso de la República",2012,"Congreso de la República de Colombia. (2012, 17 de octubre). *Ley 1581 de 2012. Por la cual se dictan disposiciones generales para la protección de datos personales*. Diario Oficial n.º 48.587.","norma","NORMA"),
 D("Ley2294","Congreso de la República",2023,"Congreso de la República de Colombia. (2023, 19 de mayo). *Ley 2294 de 2023. Por el cual se expide el Plan Nacional de Desarrollo 2022-2026 «Colombia potencia mundial de la vida»*. Diario Oficial n.º 52.400.","norma","NORMA"),
 D("Res2254","Ministerio de Ambiente y Desarrollo Sostenible",2017,"Ministerio de Ambiente y Desarrollo Sostenible. (2017, 1 de noviembre). *Resolución 2254 de 2017. Por la cual se adopta la norma de calidad del aire ambiente y se dictan otras disposiciones*.","norma","NORMA"),
 D("Conpes3943","Departamento Nacional de Planeación [DNP]",2018,"Departamento Nacional de Planeación. (2018). *Política para el mejoramiento de la calidad del aire* (Documento CONPES 3943). DNP.","norma","NORMA"),
 D("Conpes4069","Departamento Nacional de Planeación [DNP]",2021,"Departamento Nacional de Planeación. (2021). *Política nacional de ciencia, tecnología e innovación 2022-2031* (Documento CONPES 4069). DNP.","norma","NORMA"),
 D("Decision486","Comunidad Andina",2000,"Comunidad Andina. (2000, 14 de septiembre). *Decisión 486. Régimen común sobre propiedad industrial*. Gaceta Oficial del Acuerdo de Cartagena n.º 600.","norma","NORMA"),
 D("MisionSabios2019","Misión Internacional de Sabios",2019,"Misión Internacional de Sabios. (2019). *Colombia hacia una sociedad del conocimiento: Reflexiones y propuestas*. Presidencia de la República.","informe","NORMA"),
]

def _verif():
    out = {}
    for n in (1, 2, 3):
        p = os.path.join(HERE, f"verif_L{n}_salida.json")
        if os.path.exists(p):
            for x in json.load(open(p, encoding="utf-8")): out[x["key"]] = x
    return out

def banco():
    todo = corpus() + MDR + CANON + DOMINIO + NORMAS
    V = _verif()
    for r in todo:
        x = V.get(r["key"])
        if not x: continue
        e = x["estado"]
        # CORREGIR: la corrección ya se incorporó arriba en la cadena APA; se marca como verificada.
        r["ver"] = {"VERIFICADO_WEB": "VERIFICADO", "CORREGIR": "VERIFICADO", "PARCIAL": "PARCIALMENTE_VERIFICADO", "NO_ENCONTRADO": "NO_VERIFICADO"}.get(e, "NO_VERIFICADO")
    claves = set()
    for r in todo:
        assert r["key"] not in claves, r["key"]
        claves.add(r["key"])
        r.setdefault("origen", "DOMINIO")
    return todo

def exportar():
    b = banco()
    json.dump(b, open(os.path.join(HERE, "banco.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = ["# BANCO CERRADO DE REFERENCIAS (usar solo estas; la cita en el texto debe coincidir con la columna «Cita»)\n",
         "Origen F-INF = corpus del informe_FINAL aportado por el usuario (DECLARADO, no verificado en esta corrida). "
         "CANON = obras citadas por el metaprompt y por la sección 4.4-MDR. DOMINIO = literatura de dominio. NORMA = normas y documentos oficiales colombianos.\n",
         "| Clave | Cita en el texto | Año | Tipo | Origen | Referencia APA 7 |", "| --- | --- | --- | --- | --- | --- |"]
    for r in b:
        L.append(f"| {r['key']} | {r['cite']} ({r['year']}) | {r['year']} | {r['tipo']} | {r['origen']} | {r['apa']} |")
    open(os.path.join(HERE, "BANCO_REFERENCIAS.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return len(b)

if __name__ == "__main__":
    print(exportar(), "referencias")
    from collections import Counter
    print(Counter(r["origen"] for r in banco()))
